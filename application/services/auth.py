import calendar
import datetime

import jwt
from flask import abort

from application.helpers.constants import JWT_SECRET, JWT_ALGORITHM
from application.services.user import UserService


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_tokens(self, username, password):
        user = self.user_service.get_by_username(username)

        if user is None:
            raise abort(404)

        if not self.user_service.compare_passwords(user.password, password):
            abort(400)

        data = {
            "username": user.username,
            "role": user.role
        }

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }
