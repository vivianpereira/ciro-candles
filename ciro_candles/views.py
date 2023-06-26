from flask import Blueprint, render_template, request, redirect
from .models import products

bp = Blueprint("main", __name__)


@bp.route("/home/")
def home():
    return render_template("index.html")


@bp.route("/")
def index():
    return redirect("/home")


@bp.route("/category/<name>")
def category(name):
    if name == "candles":
        return render_template(
            "category.html",
            products=filter(lambda product: product.category == "candle", products),
            category=name.capitalize(),
        )
    elif name == "diffusers":
        return render_template(
            "category.html",
            products=filter(lambda product: product.category == "diffuser", products),
            category=name.capitalize(),
        )


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
