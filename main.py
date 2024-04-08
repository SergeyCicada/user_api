from flask_restx import Api
from app.config import Config
from app.database import db
from flask import Flask
from flask_migrate import Migrate

from app.views.users import user_ns


def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()

    return application


def configure_app(application: Flask):
    db.init_app(application)
    api = Api(app)
    api.add_namespace(user_ns)


app_config = Config()
app = create_app(app_config)
migrate = Migrate(app, db)
configure_app(app)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
