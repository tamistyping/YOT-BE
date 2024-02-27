from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Status
from .serializers import StatusSerializer

def view_status(request, status_id):
    status = get_object_or_404(Status, pk=status_id)
    return render(request, 'view_status.html', {'status': status})

def add_status(request):
    if request.method == 'POST':
        serializer = StatusSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('status_detail', status_id=serializer.data['id'])
        return JsonResponse(serializer.errors, status=400)
    return render(request, 'add_status.html')

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
        return redirect('status_list')
    return render(request, 'delete_status.html', {'status': status})

