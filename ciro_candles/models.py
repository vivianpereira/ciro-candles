from . import db


class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    sub_name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(80), nullable=False)
    image = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        str = "id: {}, Name: {}, Sub_Name: {}, Description: {}, Price: {}, Category: {}, Image: {}\n"
        str = str.format(
            self.id,
            self.name,
            self.sub_name,
            self.description,
            self.price,
            self.category,
            self.image,
        )
        return str


orderdetails = db.Table(
    "orderdetails",
    db.Column("order_id", db.Integer, db.ForeignKey("orders.id"), nullable=False),
    db.Column("product_id", db.Integer, db.ForeignKey("products.id"), nullable=False),
    db.PrimaryKeyConstraint("order_id", "product_id"),
)


class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, default=False)
    firstname = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    email = db.Column(db.String(128))
    address = db.Column(db.String(50))
    state = db.Column(db.String(3))
    postcode = db.Column(db.Integer)
    date = db.Column(db.DateTime)
    totalcost = db.Column(db.Float)
    products = db.relationship("Product", secondary=orderdetails, backref="orders")

    def __repr__(self):
        str = "id: {}, Firstname: {}, Surname: {}, Email: {}, Address: {}, State: {}, Postcode: {}"
        str = str.format(
            self.id,
            self.firstname,
            self.surname,
            self.email,
            self.address,
            self.state,
            self.postcode,
        )
        return str
