from app.dao.user import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        uid = data.get("id")
        user = self.get_one(uid)

        user.username = data.get("username")
        user.age = data.get("age")

        self.dao.update(user)

    def update_partial(self, data):
        uid = data.get("id")
        user = self.get_one(uid)

        if "username" in data:
            user.username = data.get("username")
        if "age" in data:
            user.age = data.get("age")

        self.dao.update(user)

    def delete(self, uid):
        self.dao.delete(uid)
