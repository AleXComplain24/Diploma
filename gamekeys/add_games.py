from store.models import Game

games = [
    {"name": "The Witcher 3", "description": "An open-world RPG about a witcher.", "price": 29.99},
    {"name": "Prototype 2", "description": "A fast-paced action game with superhuman abilities.", "price": 19.99},
    {"name": "Cyberpunk 2077", "description": "A futuristic open-world RPG.", "price": 49.99},
    {"name": "Mortal Kombat 1", "description": "A reboot of the iconic fighting series.", "price": 59.99},
    {"name": "It Takes Two", "description": "A co-op adventure about relationships.", "price": 39.99},
    {"name": "Tekken 8", "description": "The latest installment in the Tekken fighting game series.", "price": 69.99},
]

for game_data in games:
    Game.objects.get_or_create(**game_data)
print("Games added successfully!")
