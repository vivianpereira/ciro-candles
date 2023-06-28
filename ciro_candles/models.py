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
    firstname = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    email = db.Column(db.String(128))
    address = db.Column(db.String(30))
    state = db.Column(db.String(3))
    postcode = db.Column(db.Integer)
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


# class Product:
#     def __init__(self, id, name, sub_name, description, category, price, image):
#         self.id = id
#         self.name = name
#         self.sub_name = sub_name
#         self.description = description
#         self.category = category
#         self.price = price
#         self.image = image

# p1 = Product(name='Bling Candle', sub_name='Bling Candle - Pyrite Infused', description='Light up your space with the added glitz and glamour of Beautiful Bling - the perfect way to add a touch of sophistication and style to your home.<br>Natural soy wax<br>50+hr burn time', price=39.00, category='candle', image='images/candles/candle1.webp')

# p2 = Product(name='Personalised Birthday Candle', sub_name='Personalised Birthday Candle - Pyrite Infused', description='This candle is the perfect way to celebrate a special birthday. Personalise it with your loved one name and watch as they make a wish and blow out the candle, surrounded by the aroma of their favorite scent.', price=59.00, category='candles', image='images/candles/candle2.webp')

# p3 = Product(name='Crystal Candle', sub_name='Turquoise Howlite Crystal Candle', description='Turquoise Howlite Crystal Candle is a perfect blend of soothing scents and calming energy. With the gentle aroma of lavender, rosemary, vanilla bean and patchouli.', price=47.00, category='candles', image='images/candles/candle3.webp')

# p4 = Product(name='Happy Wishes Crystal Candle', sub_name='Happy Wishes Crystal Candle - Selenite, Black Tourmaline and Amethyst Infusion', description='Infused with three powerful crystals, Selenite, Black Tourmaline, and Amethyst, this candle helps to cleanse and protect your space, while promoting positive energy.', price=63.00, category='candles', image='images/candles/candle3.webp')

# p5 = Product(name='Moonstone Crystal Diffuser', sub_name='Moonstone Crystal Diffuser', description='This diffuser is exclusively designed and handcrafted by Enchanting Aromas, combining beautiful fragrances and natural crystals to create a unique experience. Bring the enchanting energy of the Moonstone into your life with our Crystal Infused fragrance diffuser - 200ml diffuser - 1 set of five diffuser sticks.', price=58.00, category='diffuser', image='images/diffusers/diffuser1.webp')

# p6 = Product(name='Rhodonite Crystal Diffuser', sub_name='Rhodonite Crystal Diffuser', description='A luxurious addition to any home or a perfect gift for someone special. The stunning pink hues of Rhodonite are not just visually appealing but also connected to the heart chakras, promoting authentic and healthy love while overcoming fear - 200ml diffuser - 1 set of five diffuser sticks.', price=56.00, category='diffuser', image='images/diffusers/diffuser2.webp')

# p7 = Product(name='Turquoise Crystal Diffuser', sub_name='Turquoise Crystal Diffuser', description='Turquoise Crystal Gemstone Diffuser is the perfect combination of captivating scent and soothing energy. With the infusion of crystal energy, this diffuser provides a unique and calming experience - 200ml diffuser - 1 set of five diffuser sticks.', price=52.00, category='diffuser', image='images/diffusers/diffuser3.webp')

# p8 = Product(name='Tiger Eye Crystal Diffuser', sub_name='Tiger Eye Crystal Diffuser', description='With the powers of protection and the spirit of the tiger, this diffuser will fill your space with an earthly rich and curious peace - 200ml diffuser - 1 set of five diffuser sticks.', price=50.00, category='diffuser', image='images/diffusers/diffuser4.webp')

# products = [p1, p2, p3, p4, p5, p6, p7, p8]
products = []
