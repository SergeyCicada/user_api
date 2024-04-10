from flask import jsonify, request
from flask_restx import Namespace, Resource

from application.container import user_service
from application.dao.models.user import UserSchema
from application.helpers.decorators import admin_required

user_ns = Namespace('users')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route('/')
class UsersView(Resource):
    def get(self):
        all_users = user_service.get_all()

        return users_schema.dump(all_users), 200

    def post(self):
        req_json = request.json
        user = user_service.create(req_json)

        return "", 201


@user_ns.route('/<int:uid>')
class UserView(Resource):
    def get(self, uid: int):
        user = user_service.get_one(uid)

        return user_schema.dump(user), 200

    def put(self, uid: int):
        req_json = request.json
        req_json["id"] = uid
        user_service.update(req_json)

        return "", 201

    def patch(self, uid: int):
        req_json = request.json
        req_json["id"] = uid
        user_service.update_partial(req_json)

        return "", 204

    @admin_required
    def delete(self, uid: int):
        user_service.delete(uid)

        return "", 204
