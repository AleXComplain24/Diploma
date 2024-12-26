from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    name = models.CharField(max_length=100)       # Название игры (строка до 100 символов)
    description = models.TextField()             # Описание игры (длинный текст)
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Цена игры с двумя знаками после запятой

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cart")
    games = models.ManyToManyField(Game, related_name="carts")

    def total_price(self):
        return sum(game.price for game in self.games.all())

    def __str__(self):
        return f"Cart of {self.user.username}"