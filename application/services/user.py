import base64
import hashlib
import hmac

from application.dao.user import UserDAO
from application.helpers.constants import PWD_SALT, PWD_ITERATIONS


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_by_username(self, username):
        return self.dao.get_by_username(username)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        data["password"] = self.generate_password(data["password"])
        return self.dao.create(data)

    def update(self, data):
        uid = data.get("id")
        user = self.get_one(uid)

        user.username = data.get("username")
        user.age = data.get("age")
        user.password = self.generate_password(data.get("password"))
        user.role = data.get("role")

        self.dao.update(user)

    def update_partial(self, data):
        uid = data.get("id")
        user = self.get_one(uid)

        if "username" in data:
            user.username = data.get("username")
        if "age" in data:
            user.age = data.get("age")
        if "password" in data:
            user.password = self.generate_password(data.get("password"))
        if "role" in data:
            user.role = data.get("role")

        self.dao.update(user)

    def delete(self, uid):
        self.dao.delete(uid)

    def generate_password(self, password):
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_SALT,
            PWD_ITERATIONS
        )
        return base64.b64encode(hash_digest)

    def compare_passwords(self, password_hash, other_password) -> bool:
        decoded_digest = base64.b64decode(password_hash)

        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            other_password.encode('utf-8'),
            PWD_SALT,
            PWD_ITERATIONS
        )
        return hmac.compare_digest(decoded_digest, hash_digest)


