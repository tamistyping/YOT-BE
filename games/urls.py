from django.urls import path
from . import views

urlpatterns = [
    path('top-rated-games/', views.top_rated_games, name='top_rated_games'),
    path('top-anticipated-games/', views.top_anticipated_games, name='top_anticipated_games'),
    path('search-games/', views.search_games, name='search_games'),
]
