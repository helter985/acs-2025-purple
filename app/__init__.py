from flask import Flask
from flask_cors import CORS
import os

from app.config import SECRET_KEY, UPLOAD_FOLDER

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    
    CORS(app)
    
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    
    from app.routes.productos import productos_bp
    
    app.register_blueprint(productos_bp, url_prefix='/v1')
    
    @app.route('/v1/healthcheck', methods=['GET'])
    def healthcheck():
        return {"status": "OK", "version": "1.0.0"}, 200
    
    return app 