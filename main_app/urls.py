from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('games/', views.game_index, name='game-index'),
  path('games/<int:game_id>/', views.game_detail, name='game-detail'),
  path('cats/create/', views.GameCreate.as_view(), name='game-create'),
]