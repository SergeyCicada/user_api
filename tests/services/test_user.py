from unittest.mock import MagicMock

import pytest

from application.dao.models.user import User
from application.dao.user import UserDAO
from application.services.user import UserService


@pytest.fixture()
def user_dao():
    user_dao = UserDAO(None)

    john = User(id=1, username="John", age=23)
    kate = User(id=2, username="Kate", age=26)
    max = User(id=3, username="Max", age=31)

    user_dao.get_one = MagicMock(return_value=john)
    user_dao.get_by_username = MagicMock(return_value={
        "username": "John",
        "age": 23
    })
    user_dao.get_all = MagicMock(return_value=[john, kate, max])
    user_dao.create = MagicMock(return_value=User(id=3))
    user_dao.delete = MagicMock()
    user_dao.update = MagicMock()

    return user_dao


class TestUserSrvice:
    @pytest.fixture(autouse=True)
    def user_service(self, user_dao):
        self.user_service = UserService(dao=user_dao)

    def test_get_one(self):
        user = self.user_service.get_one(1)

        assert user is not None
        assert user.id is not None
        assert user.username == "John"

    def test_get_username(self):
        user = self.user_service.get_by_username(3)

        assert user["username"] == "John"

    def test_get_all(self):
        user = self.user_service.get_all()

        assert len(user) > 0

    def test_create(self):
        new_user = {
            "name": "Ivan",
            "age": 39,
            "password": "123"
        }

        user = self.user_service.create(new_user)

    def test_delete(self):
        self.user_service.delete(1)

    def test_update(self):
        new_user = {
            "id": 3,
            "name": "Ivan",
            "age": 39,
            "password": "123"
        }

        self.user_service.update(new_user)
