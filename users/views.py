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
        return JsonResponse({'message': 'Game added to collection'}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
def remove_from_collection(request, game_id):
    if request.method == 'DELETE':
        try:
            user = request.user
            user.game_collection.remove(game_id)
            return JsonResponse({'message': 'Game deleted from collection successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Only DELETE requests are allowed'}, status=405)
    
@csrf_exempt
def get_collection(request):
    if request.method != 'GET':
        return JsonResponse({'error': 'Only GET method allowed'}, status=405)

    try:
        user = request.user
        game_ids = user.game_collection 
        return JsonResponse({'game_ids': game_ids}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)