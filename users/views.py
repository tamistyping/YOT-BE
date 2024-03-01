import os
import boto3
import uuid
from django.shortcuts import redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
import json


@csrf_exempt
def add_to_collection(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST method allowed'}, status=405)

    data = json.loads(request.body)
    game_id = data.get('game_id')

    if not game_id:
        return JsonResponse({'error': 'Game ID is required'}, status=400)

    try:
        user = request.user
        user.game_collection.append(game_id)  
        user.save() 
        return JsonResponse({'message': 'Game added to collection'}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
def remove_from_collection(request, game_id):
    if request.method == 'DELETE':
        try:
            user = request.user
            user.game_collection.remove(game_id) 
            user.save()  
            return JsonResponse({'message': 'Game deleted from collection successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Only DELETE requests are allowed'}, status=405)
    
@csrf_exempt
def add_photo(request, user_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['AWS_STORAGE_BUCKET_NAME']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"https://{bucket}.s3.amazonaws.com/{key}"
            user = User.objects.get(pk=user_id)
            user.profile_picture = url 
            user.save()
            return JsonResponse({'message': 'Profile picture added successfully', 'url': url}, status=200)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
            return JsonResponse({'error': 'Failed to upload profile picture'}, status=500)
    else:
        return JsonResponse({'error': 'No file provided'}, status=400)
