from django.urls import path
from . import views  # Общий импорт для доступа ко всем представлениям через views
from .views import remove_from_cart
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.game_list, name='game_list'),  # Главная страница выводит (список игр)
    path('<int:pk>/', views.game_detail, name='game_detail'),  # Страница игры по ID
    path('store/', views.store_game_list, name='store_game_list'),  # Страница магазина  # Страница магазина
    path('<int:pk>/add_to_cart/', views.add_to_cart, name='add_to_cart'),  # Добавить в корзину
    path('cart/', views.cart, name='cart'),  # Страница корзины
    path('remove-from-cart/<int:game_id>/', views.remove_from_cart, name='remove_from_cart'), # Указание game_id в маршруте
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('checkout/', views.checkout, name='checkout'),  # Новый маршрут для оформления заказа
    path('process-order/', views.process_order, name='process_order'),  # Добавить маршрут для обработки заказа
]