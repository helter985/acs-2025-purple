from flask import Flask
from flask_cors import CORS

from app.config import SECRET_KEY, DATABASE_URL
from app.models.db import db

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSON_AS_ASCII'] = False  # Permitir caracteres UTF-8 en JSON
    
    CORS(app)
    db.init_app(app)
        
    from app.routes.producto_routes import productos_bp
    
    app.register_blueprint(productos_bp, url_prefix='/v1')
    
    with app.app_context():
        db.create_all()
    
    @app.route('/v1/healthcheck', methods=['GET'])
    def healthcheck():
        return {"status": "OK", "version": "1.0.0"}, 200
    
    return app 