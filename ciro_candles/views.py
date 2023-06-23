from flask import Blueprint, render_template, request, redirect

bp = Blueprint("main", __name__)

class Product:
  def __init__(self, id, name, description, category, price, image):
    self.id = id
    self.name = name
    self.description = description
    self.category = category
    self.price = price
    self.image = image

class Order:
  def __init__(self, id):
    self.id = id

class Order_Details:
  def __init__(self, id):
    self.id = id

p1 = Product(1, "Bling Candle - Pyrite Infused", "Light up your space with the added glitz and glamour of Beautiful Bling - the perfect way to add a touch of sophistication and style to your home.<br>Natural soy wax<br>50+hr burn time", "candle", "$39.00 AUD", "images/candles/candle1.webp")
p2 = Product(2, "Candle 2", "Description 2", "candle", 200.50, "images/candles/candle2.webp")
p3 = Product(3, "Candle 3", "Description 3", "candle", 300.50, "images/candles/candle3.webp")
p4 = Product(4, "Candle 4", "Description 4", "candle", 400.50, "images/candles/candle4.webp")

p5 = Product(5, "Diffuser 1", "Desc 1", "diffuser", "$39.00 AUD", "images/diffusers/diffuser1.webp")
p6 = Product(6, "Diffuser 2", "Description 2", "diffuser", 200.50, "images/diffusers/diffuser2.webp")
p7 = Product(7, "Diffuser 3", "Description 3", "diffuser", 300.50, "images/diffusers/diffuser3.webp")
p8 = Product(8, "Diffuser 4", "Description 4", "diffuser", 400.50, "images/diffusers/diffuser4.webp")


products = [p1, p2, p3, p4, p5, p6, p7, p8]     


@bp.route("/home/")
def home():
    return render_template("index.html")

@bp.route("/")
def index():
    return redirect("/home")

@bp.route("/category/<name>")
def category(name):
    if name == "candles":
        return render_template("category.html", products=filter(lambda product: product.category == "candle", products))
    elif name == "diffusers":
        return render_template("category.html", products=filter(lambda product: product.category == "diffuser", products))

@bp.route("/detail/<id>")
def detail(id):
    index = int(id) - 1
    return render_template("detail.html", product=products[index])

@bp.route("/basket/")
def basket():
    return render_template("basket.html")

@bp.route("/checkout/", methods=["POST", "GET"])
def checkout():
    return render_template("checkout.html")
