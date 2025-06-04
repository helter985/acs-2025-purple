import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')

load_dotenv(dotenv_path, override=True)



DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@localhost:5432/purple_db')
SECRET_KEY = os.getenv('SECRET_KEY', os.urandom(24).hex())
UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'app/static/images')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'} 
