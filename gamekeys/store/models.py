from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Привязка корзины к пользователю
    game = models.ForeignKey('store.Game', on_delete=models.CASCADE) # Привязка игры
    quantity = models.PositiveIntegerField(default=1) # Количество
    def __str__(self):
        return f"{self.user.username} - {self.game.name} ({self.quantity})"

    def __str__(self):
        return f"{self.user.username} - {self.game.name} ({self.quantity})"

    def total_price(self):
        return sum(game.price for game in self.games.all())

    def __str__(self):
        return f"Cart of {self.user.username}"