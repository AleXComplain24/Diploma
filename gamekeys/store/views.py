from django.shortcuts import render
from .models import Game

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