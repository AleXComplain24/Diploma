from django.db import models
from django.contrib.auth.models import User
from store.models import Game
from .models import Cart

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.game.name}"

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, game):
        game_id = str(game.id)
        if game_id not in self.cart:
            self.cart[game_id] = {'name': game.name, 'price': str(game.price)}
        self.session.modified = True

    def remove(self, game):
        game_id = str(game.id)
        if game_id in self.cart:
            del self.cart[game_id]
            self.session.modified = True

    def clear(self):
        self.session['cart'] = {}
        self.session.modified = True
