from flask import Blueprint
from . import db
from .models import Product


bp = Blueprint("admin", __name__, url_prefix="/admin/")


# function to put some seed data in the database
@bp.route("/dbseed/")
def dbseed():
    p1 = Product(
        name="Bling Candle",
        sub_name="Bling Candle - Pyrite Infused",
        description="Light up your space with the added glitz and glamour of Beautiful Bling - the perfect way to add a touch of sophistication and style to your home.",
        price=39.00,
        category="candle",
        image="images/candles/candle1.webp",
    )
    p2 = Product(
        name="Personalised Birthday Candle",
        sub_name="Personalised Birthday Candle - Pyrite Infused",
        description="This candle is the perfect way to celebrate a special birthday. Personalise it with your loved one name and watch as they make a wish and blow out the candle, surrounded by the aroma of their favorite scent.",
        price=59.00,
        category="candles",
        image="images/candles/candle2.webp",
    )
    p3 = Product(
        name="Crystal Candle",
        sub_name="Turquoise Howlite Crystal Candle",
        description="Turquoise Howlite Crystal Candle is a perfect blend of soothing scents and calming energy. With the gentle aroma of lavender, rosemary, vanilla bean and patchouli.",
        price=47.00,
        category="candles",
        image="images/candles/candle3.webp",
    )
    p4 = Product(
        name="Happy Wishes Crystal Candle",
        sub_name="Happy Wishes Crystal Candle - Selenite, Black Tourmaline and Amethyst Infusion",
        description="Infused with three powerful crystals, Selenite, Black Tourmaline, and Amethyst, this candle helps to cleanse and protect your space, while promoting positive energy.",
        price=63.00,
        category="candles",
        image="images/candles/candle3.webp",
    )
    p5 = Product(
        name="Moonstone Crystal Diffuser",
        sub_name="Moonstone Crystal Diffuser",
        description="This diffuser is exclusively designed and handcrafted by Enchanting Aromas, combining beautiful fragrances and natural crystals to create a unique experience. Bring the enchanting energy of the Moonstone into your life with our Crystal Infused fragrance diffuser - 200ml diffuser - 1 set of five diffuser sticks.",
        price=58.00,
        category="diffuser",
        image="images/diffusers/diffuser1.webp",
    )
    p6 = Product(
        name="Rhodonite Crystal Diffuser",
        sub_name="Rhodonite Crystal Diffuser",
        description="A luxurious addition to any home or a perfect gift for someone special. The stunning pink hues of Rhodonite are not just visually appealing but also connected to the heart chakras, promoting authentic and healthy love while overcoming fear - 200ml diffuser - 1 set of five diffuser sticks.",
        price=56.00,
        category="diffuser",
        image="images/diffusers/diffuser2.webp",
    )
    p7 = Product(
        name="Turquoise Crystal Diffuser",
        sub_name="Turquoise Crystal Diffuser",
        description="Turquoise Crystal Gemstone Diffuser is the perfect combination of captivating scent and soothing energy. With the infusion of crystal energy, this diffuser provides a unique and calming experience - 200ml diffuser - 1 set of five diffuser sticks.",
        price=52.00,
        category="diffuser",
        image="images/diffusers/diffuser3.webp",
    )
    p8 = Product(
        name="Tiger Eye Crystal Diffuser",
        sub_name="Tiger Eye Crystal Diffuser",
        description="With the powers of protection and the spirit of the tiger, this diffuser will fill your space with an earthly rich and curious peace - 200ml diffuser - 1 set of five diffuser sticks.",
        price=50.00,
        category="diffuser",
        image="images/diffusers/diffuser4.webp",
    )

    try:
        db.session.add(p1)
        db.session.add(p2)
        db.session.add(p3)
        db.session.add(p4)
        db.session.add(p5)
        db.session.add(p6)
        db.session.add(p7)
        db.session.add(p8)
        db.session.commit()
    except:
        return "There was an issue adding the cities in dbseed function"

    return "DATA LOADED"
