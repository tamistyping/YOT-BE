from django.urls import path
from . import views

urlpatterns = [
    path('statuses', views.Status_index),
    path('statuses/create', views.add_status),
    path('statuses/<int:pk>/update/', views.edit_status),
    path('statuses/<int:pk>/delete/', views.delete_status),
]