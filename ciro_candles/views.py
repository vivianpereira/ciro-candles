from flask import Blueprint, render_template, request, redirect

bp = Blueprint("main", __name__)

@bp.route("/home/")
def home():
    return render_template("index.html")

@bp.route("/")
def index():
    return redirect("/home")

@bp.route("/category/<name>")
def category(name):
    return render_template("category.html")

@bp.route("/detail/")
def detail():
    return render_template("detail.html")

@bp.route("/basket/")
def basket():
    return render_template("basket.html")

@bp.route("/checkout/", methods=["POST", "GET"])
def checkout():
    return render_template("checkout.html")
