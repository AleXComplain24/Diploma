from django.shortcuts import render, redirect, get_object_or_404
from .models import Game, Cart
from .cart import Cart  # Импорт вашей корзины (если используется)


def game_list(request):
    games = Game.objects.all()  # Получаем список всех игр
    return render(request, 'store/game_list.html', {'games': games})  # Передаем в шаблон

def game_detail(request, pk):
    game = Game.objects.get(id=pk)  # Получаем конкретную игру по ее ID
    return render(request, 'store/game_detail.html', {'game': game})  # Передаем в шаблон

def game_list(request):
    return render(request, 'store/game_list.html')

def store_game_list(request):
    games = Game.objects.all()  # Получаем все игры из базы данных
    return render(request, 'store/store_game_list.html', {'games': games})

def cart(request):
    # Здесь предполагается, что корзина будет храниться в сессии
    cart_items = []  # Получение корзины (пока пусто)
    total_price = sum(item.game.price for item in cart_items)
    return render(request, 'store/cart.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, pk):
    game = get_object_or_404(Game, pk=pk)  # Получаем игру
    cart = Cart(request)  # Подключаем корзину
    cart.add(game)  # Добавляем игру в корзину
    return redirect('game_list')  # Возвращаемся на страницу магазина

def cart_view(request):
    if not request.user.is_authenticated:
        return redirect("login")
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, "store/cart.html", {"cart": cart})