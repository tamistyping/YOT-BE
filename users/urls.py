from django.urls import path
from . import views

urlpatterns = [
path('api/v1/users/<int:user_id>/add_photo/', views.add_photo, name='add_photo'),
]
