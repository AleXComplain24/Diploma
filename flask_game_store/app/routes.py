from flask import render_template, redirect, url_for, session, request
from app import app  # Используем существующий экземпляр Flask из __init__.py

# Список игр
games = [
    {"id": 1, "name": "The Witcher 3: Wild Hunt", "price": 29.99},
    {"id": 2, "name": "Cyberpunk 2077", "price": 59.99},
    {"id": 3, "name": "Elden Ring", "price": 49.99},
    {"id": 4, "name": "Dark Souls III", "price": 39.99},
    {"id": 5, "name": "Minecraft", "price": 19.99},
]

# Главная страница
@app.route("/")
def index():
    return render_template("index.html")

# Страница каталога
@app.route("/catalog")
def catalog():
    return render_template("catalog.html", games=games)

# Добавление игры в корзину
@app.route("/add-to-cart/<int:game_id>", methods=["POST"])
def add_to_cart(game_id):
    cart = session.get("cart", [])
    for game in games:
        if game["id"] == game_id:
            cart.append(game)
            break
    session["cart"] = cart
    return redirect(url_for("cart"))

# Страница корзины
@app.route("/cart")
def cart():
    cart = session.get("cart", [])
    total_price = sum(item["price"] for item in cart)
    return render_template("cart.html", cart=cart, total_price=total_price)

# Удаление игры из корзины
@app.route("/remove-from-cart/<int:game_id>", methods=["POST"])
def remove_from_cart(game_id):
    cart = session.get("cart", [])
    cart = [item for item in cart if item["id"] != game_id]
    session["cart"] = cart
    return redirect(url_for("cart"))

# Страница оформления заказа
@app.route("/checkout")
def checkout():
    cart = session.get("cart", [])
    total_price = sum(item["price"] for item in cart)
    return render_template("checkout.html", cart=cart, total_price=total_price)

# Подтверждение заказа
@app.route("/confirm-order", methods=["POST"])
def confirm_order():
    session.pop("cart", None)  # Очистка корзины
    return redirect(url_for("index"))
