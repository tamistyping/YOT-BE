from django.urls import path
from . import views

urlpatterns = [
    path('collection/add/', views.add_to_collection, name='add_to_collection'),
    path('collection/remove/', views.remove_from_collection, name='remove_from_collection'),
    path('collection/', views.get_collection, name='get_collection'),
]