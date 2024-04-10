from application.dao.user import UserDAO
from application.database import db
from application.services.user import UserService

user_dao = UserDAO(db.session)
user_service = UserService(user_dao)
