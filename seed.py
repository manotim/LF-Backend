from faker import Faker
from main import app
from models import db, Furniture, Customer, Owner
import random

fake = Faker()

with app.app_context():
# def seed_database():

    Furniture.query.delete()

    furnitures = [
        {"name": "Sofa Set", "description": "gives the wielder super-human strengths", "price":545.5, "category": "chairs", "image": "https://m.media-amazon.com/images/I/71mKwaKglhL.jpg"},
        {"name": "Traditional Table", "description": "This dining table is made with Australian Marri timber and its origins are evident in the textured grain.", "price":548.8, "category": "tables", "image": "https://www.ikea.com/in/en/images/products/nodeland-coffee-table-medium-brown__0974637_pe812499_s5.jpg"},
        {"name": "Contemporary Table", "description": "Table 100cm, which cleverly acts as a generous workspace for one then magically transforms into a dinner table", "price":544.8, "category": "tables", "image": "https://assets.nickscali.com/media/catalog/product/cache/cbdcdb92c76a5919d24cc3e60ff4de09/b/y/byron_dt_1920x1200.jpg"},
        {"name": "Bunk bed", "description": "A bunk bed or set of bunks is a type of bed in which one bed frame is stacked on top of another", "price":542.3, "category": "beds", "image": "https://m.media-amazon.com/images/I/61ep3xgFcaL.jpg"},
        {"name": "Office chair", "description": "Put simply, an office chair is a seat designed for use in an office or workspace.", "price":541.1, "category": "chairs", "image": "https://grandrapidschair.com/wp-content/uploads/2020/08/W530_Sigsbee_Chair_Front.jpg"}
    ]
    for furniture_data in furnitures:
        furniture = Furniture(name=furniture_data["name"], description=furniture_data["description"], price=furniture_data["price"], category=furniture_data["category"], image=furniture_data["image"])
        db.session.add(furniture)

    db.session.commit()

    Customer.query.delete()

    customers = [
        {"name": "Collins James", "contact": 724556789, "address":"p.o box 453 nrb", "email": "james@gmail.com", "password": "fr3rF333#"},
        {"name": "Ellias Eli", "contact": 768456123, "address":"p.o box 548 nyk", "email": "ellias@gmail.com", "password": "35345hyh^4"},
        {"name": "Lyn Ozil", "contact": 795324678, "address":"p.o box 48 ksm", "email": "lyn@gmail.com", "password": "fefk4@4"},
        
    ]
    for customer_data in customers:
        customer = Customer(name=customer_data["name"], contact=customer_data["contact"], address=customer_data["address"], email=customer_data["email"], password=customer_data["password"])
        db.session.add(customer)

    db.session.commit()

    Owner.query.delete()
    owners = [
        {"name": "Kamala Khan", "location": "Nairobi", "address": "P.O. 50412 Nrb"}
    ]
    for owner_data in owners:
        owner = Owner(name=owner_data["name"], location=owner_data["location"], address=owner_data["address"])
        db.session.add(owner)

    db.session.commit()

    # strengths = ["Strong", "Weak", "Average"]
    # all_powers = Power.query.all()

    # for hero in Hero.query.all():
    #     for  i in range(fake.random_int(min=1, max=8)):
    #         power = fake.random_element(all_powers)
    #         hero_power = HeroPower(hero=hero, power=power, strength=fake.random_element(strengths))
    #         db.session.add(hero_power)

    # db.session.commit()

    # print("🦸‍♀️ Done seeding!")