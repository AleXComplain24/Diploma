from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_list, name='game_list'),  # Главная страница выводит (список игр)
    path('<int:pk>/', views.game_detail, name='game_detail'),  # Страница игры по ID
path('store/', views.store_game_list, name='store_game_list'),  # Страница магазина
    path('cart/', views.cart, name='cart'),  # Страница корзины
]