from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from flask_login import UserMixin

db = SQLAlchemy()


class Furniture(db.Model, SerializerMixin):
    __tablename__ = 'furnitures'

    serialize_rules = ('-purchases.furniture',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    price = db.Column(db.Float)
    image = db.Column(db.String)
    category = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    purchases = db.relationship('Purchase', backref='furniture')


class Customer(db.Model,  UserMixin):
    __tablename__ = 'customers'

    serialize_rules = ('-purchases.customer',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    contact = db.Column(db.Integer)
    address = db.Column(db.String)
    email = db.Column(db.String(40), unique=True)
    password = db.Column(db.String(200))
    purchases = db.relationship('Purchase', backref='customer')
    

    

class Owner(db.Model, SerializerMixin):
    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    location = db.Column(db.String)
    address = db.Column(db.String)


  

class Purchase(db.Model, SerializerMixin):
    __tablename__ = 'purchases'

    serialize_rules = ('-furniture.purchases', '-customer.purchases',)

    id = db.Column(db.Integer, primary_key=True)
    furniture_id = db.Column(db.Integer, db.ForeignKey('furnitures.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    

 


