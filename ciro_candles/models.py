class Product:
    def __init__(self, id, name, sub_name, description, category, price, image):
        self.id = id
        self.name = name
        self.sub_name = sub_name
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


p1 = Product(
    1,
    "Bling Candle",
    "Bling Candle - Pyrite Infused",
    "Light up your space with the added glitz and glamour of Beautiful Bling - the perfect way to add a touch of sophistication and style to your home.<br>Natural soy wax<br>50+hr burn time",
    "candle",
    "$39.00 AUD",
    "images/candles/candle1.webp",
)
p2 = Product(
    2,
    "Personalised Birthday Candle",
    "Personalised Birthday Candle - Pyrite Infused",
    "This candle is the perfect way to celebrate a special birthday. Personalise it with your loved one's name and watch as they make a wish and blow out the candle, surrounded by the aroma of their favorite scent.<br>Natural soy wax<br>48+hr burn time",
    "candle",
    "$59.00 AUD",
    "images/candles/candle2.webp",
)
p3 = Product(
    3,
    "Crystal Candle",
    "Turquoise Howlite Crystal Candle",
    "Turquoise Howlite Crystal Candle is a perfect blend of soothing scents and calming energy. With the gentle aroma of lavender, rosemary, vanilla bean and patchouli.<br>Natural soy wax<br>48+hr burn time",
    "candle",
    "$47.00 AUD",
    "images/candles/candle3.webp",
)
p4 = Product(
    4,
    "Happy Wishes Crystal Candle",
    "Happy Wishes Crystal Candle - Selenite, Black Tourmaline and Amethyst Infusion",
    "Infused with three powerful crystals, Selenite, Black Tourmaline, and Amethyst, this candle helps to cleanse and protect your space, while promoting positive energy.<br>Natural soy wax<br>50+hr burn time",
    "candle",
    "$63.00 AUD",
    "images/candles/candle4.webp",
)

p5 = Product(
    5,
    "Moonstone Crystal Diffuser",
    "Moonstone Crystal Diffuser",
    "This diffuser is exclusively designed and handcrafted by Enchanting Aromas, combining beautiful fragrances and natural crystals to create a unique experience. Bring the enchanting energy of the Moonstone into your life with our Crystal Infused fragrance diffuser.<br>200ml diffuser<br>1 set of five diffuser sticks",
    "diffuser",
    "$58.00 AUD",
    "images/diffusers/diffuser1.webp",
)
p6 = Product(
    6,
    "Rhodonite Crystal Diffuser",
    "Rhodonite Crystal Diffuser",
    "A luxurious addition to any home or a perfect gift for someone special. The stunning pink hues of Rhodonite are not just visually appealing but also connected to the heart chakras, promoting authentic and healthy love while overcoming fear.<br>200ml diffuser<br>1 set of five diffuser sticks",
    "diffuser",
    "$56.00 AUD",
    "images/diffusers/diffuser2.webp",
)
p7 = Product(
    7,
    "Turquoise Crystal Diffuser",
    "Turquoise Crystal Diffuser",
    "Turquoise Crystal Gemstone Diffuser is the perfect combination of captivating scent and soothing energy. With the infusion of crystal energy, this diffuser provides a unique and calming experience.<br>200ml diffuser<br>1 set of five diffuser sticks",
    "diffuser",
    "$52.00 AUD",
    "images/diffusers/diffuser3.webp",
)
p8 = Product(
    8,
    "Tiger Eye Crystal Diffuser",
    "Tiger Eye Crystal Diffuser",
    "With the powers of protection and the spirit of the tiger, this diffuser will fill your space with an earthly rich and curious peace.<br>200ml diffuser<br>1 set of five diffuser sticks",
    "diffuser",
    "$50.00 AUD",
    "images/diffusers/diffuser4.webp",
)


products = [p1, p2, p3, p4, p5, p6, p7, p8]
