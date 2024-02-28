from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Status
from django.core.serializers import serialize
from .serializers import StatusSerializer
import json

def view_status(request):
    statuses = Status.objects.order_by('-created_at')  
    serializer = StatusSerializer(statuses, many=True)
    return JsonResponse(serializer.data, safe=False)

def add_status(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = StatusSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

def edit_status(request, status_id):
    status = get_object_or_404(Status, pk=status_id)
    if request.method == 'PUT':
        content = request.POST.get('content')
        if content:
            status.content = content
            status.save()
            return redirect('status_detail', status_id=status_id)
    return render(request, 'edit_status.html', {'status': status})

def delete_status(request, status_id):
    status = get_object_or_404(Status, pk=status_id)
    if request.method == 'DELETE':
        status.delete()
        return JsonResponse({'message': 'Status deleted successfully'})
    return JsonResponse({'error': 'Only DELETE requests are allowed'}, status=405)

