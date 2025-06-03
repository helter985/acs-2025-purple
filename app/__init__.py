from flask import Flask
from flask_cors import CORS
import os

from app.config import SECRET_KEY, UPLOAD_FOLDER, DATABASE_URL
from app.models.db import db, init_db

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    CORS(app)
    db.init_app(app)
    
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    
    from app.routes.productos import productos_bp
    
    app.register_blueprint(productos_bp, url_prefix='/v1')
    
    with app.app_context():
        db.create_all()
    
    @app.route('/v1/healthcheck', methods=['GET'])
    def healthcheck():
        return {"status": "OK", "version": "1.0.0"}, 200
    
    return app 