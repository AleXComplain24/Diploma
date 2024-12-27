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
    if request.method == "POST":
        # Получаем элемент корзины с указанным game_id
        cart_item = get_object_or_404(Cart, game_id=game_id)
        cart_item.delete()  # Удаляем элемент корзины
    return redirect('cart')  # Перенаправляем пользователя обратно в корзину


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

@login_required
def checkout(request):
    """
    Страница оформления заказа.
    """
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.game.price * item.quantity for item in cart_items)
    return render(request, 'store/checkout.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })

def process_order(request):
    """
    Обработка заказа после нажатия на кнопку подтверждения.
    """
    if request.method == 'POST' and request.user.is_authenticated:
        # Здесь вы можете реализовать логику для обработки заказа
        # Например: сохранить данные о заказе в базе данных
        Cart.objects.filter(user=request.user).delete()  # Очищаем корзину после оформления заказа
        return redirect('game_list')  # Перенаправляем пользователя на главную страницу или список игр
    return redirect('checkout')  # В случае GET-запроса или ошибки возвращаемся на страницу оформления