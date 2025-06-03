from flask_sqlalchemy import SQLAlchemy
from app.config import DATABASE_URL

db = SQLAlchemy()

def init_db(app):
    """Initialize the database with SQLAlchemy"""
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config.get('DATABASE_URL', DATABASE_URL)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
        print("Base de datos inicializada correctamente") 