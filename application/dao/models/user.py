from marshmallow import fields, Schema

from application.database import db


class User(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    age = db.Column(db.Integer)
    password = db.Column(db.String)
    role = db.Column(db.String)


class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    age = fields.Int()
    password = fields.Str()
    role = fields.Str()
