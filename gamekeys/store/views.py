from django.shortcuts import render, redirect, get_object_or_404
from .models import Game, Cart  # Импорт модели игры и корзины
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


def store_game_list(request):
    """
    Представление для отображения списка всех игр в магазине.
    """
    games = Game.objects.all()  # Получаем все игры из базы данных
    return render(request, 'store/store_game_list.html', {'games': games})


@csrf_exempt
@login_required
def add_to_cart(request, pk):
    game = get_object_or_404(Game, pk=pk)
    cart_item, created = Cart.objects.get_or_create(user=request.user, game=game)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

@login_required
def cart(request):
    """
    Отображение корзины пользователя.
    """
    cart_items = Cart.objects.filter(user=request.user)  # Получаем все элементы корзины текущего пользователя
    total_price = sum(item.game.price * item.quantity for item in cart_items)  # Подсчет общей стоимости
    return render(request, 'store/cart.html', {'cart_items': cart_items, 'total_price': total_price})


@csrf_exempt
@login_required
def remove_from_cart(request, game_id):
    """
    Удаление игры из корзины пользователя.
    """
    game = get_object_or_404(Game, pk=pk)  # Получаем игру
    cart_item = Cart.objects.filter(user=request.user, game=game).first()  # Получаем элемент корзины
    if cart_item:
        cart_item.delete()  # Удаляем запись из корзины
    return redirect('cart')  # Перенаправляем на страницу корзины


def game_list(request):
    """
    Отображение списка всех игр.
    """
    games = Game.objects.all()  # Получаем список всех игр
    return render(request, 'store/game_list.html', {'games': games})  # Передаем игры в шаблон


def game_detail(request, pk):
    """
    Отображение детальной информации об игре.
    """
    game = get_object_or_404(Game, pk=pk)  # Получаем конкретную игру
    return render(request, 'store/game_detail.html', {'game': game})  # Передаем игру в шаблон
