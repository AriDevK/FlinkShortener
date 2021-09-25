from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import DevelopmentConfig, ProductionConfig


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)

    with app.app_context():
        from .models import Links
        db.create_all()

    return app


app = create_app()

from app import routes