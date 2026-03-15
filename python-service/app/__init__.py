from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import os



from datetime import datetime, date
from decimal import Decimal

db = SQLAlchemy()
jwt = JWTManager()





def create_app(config_name=None):
    app = Flask(__name__)

    # Load configuration
    from app.config import get_config
    app.config.from_object(get_config(config_name))

    # Override SQLALCHEMY_DATABASE_URI with environment variable if available
    if os.environ.get('SQLALCHEMY_DATABASE_URI'):
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

    # Set custom JSON encoder


    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    CORS(app)

    # Register blueprints
    from app.routes.auth import auth_bp
    from app.routes.products import products_bp
    from app.routes.orders import orders_bp
    from app.routes.payments import payments_bp

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(products_bp, url_prefix="/api/products")
    app.register_blueprint(orders_bp, url_prefix="/api/orders")
    app.register_blueprint(payments_bp, url_prefix="/api/payments")

    # Create tables
    with app.app_context():
        from app.models import user, product, order
        db.create_all()

    return app
