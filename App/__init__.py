from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
db=SQLAlchemy()
def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    from .routes import routes as main_blueprint
    app.register_blueprint(main_blueprint)
    from .error import error as errors_blueprint
    app.register_blueprint(errors_blueprint)
    return app