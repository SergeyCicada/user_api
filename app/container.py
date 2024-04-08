from app.dao.user import UserDAO
from app.database import db
from app.services.user import UserService

user_dao = UserDAO(db.session)
user_service = UserService(user_dao)
