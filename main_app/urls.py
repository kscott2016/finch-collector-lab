from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('games/', views.game_index, name='game-index'),
  path('games/<int:game_id>/', views.game_detail, name='game-detail'),
  path('games/create/', views.GameCreate.as_view(), name='game-create'),
  path('games/<int:pk>/update/', views.GameUpdate.as_view(), name='game-update'),
  path('games/<int:pk>/delete/', views.GameDelete.as_view(), name='game-delete'),
  path('games/<int:game_id>/add-type/', views.add_type, name='add-type'),
]