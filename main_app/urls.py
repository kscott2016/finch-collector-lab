from django.urls import path
from . import views

urlpatterns = [
  # path('', views.home, name='home'),
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('games/', views.game_index, name='game-index'),
  path('games/<int:game_id>/', views.game_detail, name='game-detail'),
  path('games/create/', views.GameCreate.as_view(), name='game-create'),
  path('games/<int:pk>/update/', views.GameUpdate.as_view(), name='game-update'),
  path('games/<int:pk>/delete/', views.GameDelete.as_view(), name='game-delete'),
  path('games/<int:game_id>/add-type/', views.add_type, name='add-type'),
  path('consoles/create/', views.ConsoleCreate.as_view(), name='console-create'),
  path('consoles/<int:pk>/', views.ConsoleDetail.as_view(), name='console-detail'),
  path('consoles/', views.ConsoleList.as_view(), name='console-index'),
  path('consoles/<int:pk>/update/', views.ConsoleUpdate.as_view(), name='console-update'),
  path('consoles/<int:pk>/delete/', views.ConsoleDelete.as_view(), name='console-delete'),
  path('games/<int:game_id>/console_list/<int:console_id>/', views.console_list, name='console-list'),
]