import os
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from jinja2 import Template, Environment, FileSystemLoader

app = FastAPI()

static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Подключение статических файлов
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Шаблоны
templates = Environment(loader=FileSystemLoader("app/templates"))

# Данные приложения
games = [
    {"id": 1, "name": "The Witcher 3: Wild Hunt", "price": 29.99},
    {"id": 2, "name": "Cyberpunk 2077", "price": 59.99},
    {"id": 3, "name": "Elden Ring", "price": 49.99},
    {"id": 4, "name": "Dark Souls III", "price": 39.99},
    {"id": 5, "name": "Minecraft", "price": 19.99},
]
cart = []


@app.get("/", response_class=HTMLResponse)
async def index():
    template = templates.get_template("index.html")
    return HTMLResponse(template.render(games=games))


@app.get("/catalog", response_class=HTMLResponse)
async def catalog():
    template = templates.get_template("catalog.html")
    return HTMLResponse(template.render(games=games))


@app.post("/add-to-cart/{game_id}")
async def add_to_cart(game_id: int):
    for game in games:
        if game["id"] == game_id:
            cart.append(game)
            break
    # Перенаправляем пользователя на страницу корзины
    return RedirectResponse(url="/cart", status_code=303)


@app.get("/cart", response_class=HTMLResponse)
async def view_cart():
    total_price = sum(item["price"] for item in cart)
    template = templates.get_template("cart.html")
    return HTMLResponse(template.render(cart=cart, total_price=total_price))


@app.post("/remove-from-cart/{game_id}")
async def remove_from_cart(game_id: int):
    global cart
    cart = [item for item in cart if item["id"] != game_id]
    return RedirectResponse(url="/cart", status_code=303)


@app.get("/checkout", response_class=HTMLResponse)
async def checkout():
    total_price = sum(item["price"] for item in cart)
    template = templates.get_template("checkout.html")
    return HTMLResponse(template.render(cart=cart, total_price=total_price))


@app.post("/confirm-order")
async def confirm_order():
    global cart
    cart.clear()
    return RedirectResponse(url="/", status_code=303)

