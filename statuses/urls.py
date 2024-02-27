from django.urls import path
from . import views

urlpatterns = [
    path('statuses/', views.view_status, name='status_list'),  
    path('statuses/create/', views.add_status, name='add_status'),
    path('statuses/<int:pk>/update/', views.edit_status, name='edit_status'),
    path('statuses/<int:pk>/delete/', views.delete_status, name='delete_status'),
]