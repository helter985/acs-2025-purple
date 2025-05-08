import psycopg2
from psycopg2.extras import RealDictCursor
import os
from app.config import DATABASE_URL

def get_db_connection():
    try:
        conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
        return conn
    except Exception as e:
        print(f"Error al conectar con la base de datos: {e}")
        raise e

def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    
    cur.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id SERIAL PRIMARY KEY,
            codigo VARCHAR(50) UNIQUE NOT NULL,
            nombre VARCHAR(200) NOT NULL,
            precio FLOAT NOT NULL,
            imagen VARCHAR(255)
        )
    ''')
    
    conn.commit()
    cur.close()
    conn.close()
    
    print("Base de datos inicializada correctamente") 