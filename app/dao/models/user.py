from marshmallow import fields, Schema

from app.database import db


class User(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    age = db.Column(db.Integer)


class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    age = fields.Int()
