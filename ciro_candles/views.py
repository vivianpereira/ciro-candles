from flask import Blueprint, render_template, url_for, request, session, flash, redirect
from .models import Product, Order
from datetime import datetime
from .forms import CheckoutForm
from . import db

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
            products=Product.query.filter(Product.category == "candles"),
            category=name.capitalize(),
        )
    elif name == "diffusers":
        return render_template(
            "category.html",
            products=Product.query.filter(Product.category == "diffuser"),
            category=name.capitalize(),
        )


@bp.route("/detail/<int:id>")
def detail(id):
    return render_template("detail.html", product=Product.query.get(id))


@bp.route("/basket/", methods=["POST", "GET"])
def basket():
    product_id = request.values.get("product_id")

    # retrieve order if there is one
    if "order_id" in session.keys():
        order = Order.query.get(session["order_id"])
        # order will be None if order_id stale
    else:
        # there is no order
        order = None

    # create new order if needed
    if order is None:
        order = Order(
            status=False,
            firstname="",
            surname="",
            address="",
            state="",
            postcode=0,
            totalcost=0,
            date=datetime.now(),
        )
        try:
            db.session.add(order)
            db.session.commit()
            session["order_id"] = order.id
        except:
            print("failed at creating a new order")
            order = None

    # calcultate totalprice
    totalprice = 0
    if order is not None:
        for product in order.products:
            totalprice = totalprice + product.price

    # are we adding an item?
    if product_id is not None and order is not None:
        product = Product.query.get(product_id)
        if product not in order.products:
            try:
                order.products.append(product)
                db.session.commit()
            except:
                return "There was an issue adding the item to your basket"
            return redirect(url_for("main.basket"))
        else:
            flash("item already in basket")
            return redirect(url_for("main.basket"))

    return render_template("basket.html", order=order, totalprice=totalprice)


# Delete item of the basket
@bp.route("/deletebasketitem", methods=["POST"])
def deletebasketitem():
    id = request.form["id"]
    if "order_id" in session:
        order = Order.query.get_or_404(session["order_id"])
        product_to_delete = Product.query.get(id)
        try:
            order.products.remove(product_to_delete)
            db.session.commit()
            return redirect(url_for("main.basket"))
        except:
            return "Problem deleting item from order"
    return redirect(url_for("main.order"))


# Scrap basket
@bp.route("/deleteorder")
def deleteorder():
    if "order_id" in session:
        del session["order_id"]
        flash("All items deleted")
    return redirect(url_for("main.index"))


@bp.route("/checkout/", methods=["POST", "GET"])
def checkout():
    form = CheckoutForm()
    if "order_id" in session:
        order = Order.query.get_or_404(session["order_id"])

        if form.validate_on_submit():
            order.status = True
            order.firstname = form.firstname.data
            order.surname = form.surname.data
            order.address = form.address.data
            order.state = form.state.data
            order.postcode = form.postcode.data
            totalcost = 0
            for product in order.products:
                totalcost = totalcost + product.price
            order.totalcost = totalcost
            order.date = datetime.now()
            try:
                db.session.commit()
                del session["order_id"]
                flash(
                    "Thank you! One of our awesome team members will contact you soon..."
                )
                return redirect(url_for("main.home"))
            except:
                return "There was an issue completing your order"
    return render_template("checkout.html", form=form)
