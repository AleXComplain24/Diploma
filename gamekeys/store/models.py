from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=100)       # Название игры (строка до 100 символов)
    description = models.TextField()             # Описание игры (длинный текст)
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Цена игры с двумя знаками после запятой

    def __str__(self):
        return self.name