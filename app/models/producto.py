from app.models.db import get_db_connection

class Producto:
    
    @staticmethod
    def obtener_todos(nombre=None):
        conn = get_db_connection()
        cursor = conn.cursor()
        
        if nombre:
            cursor.execute(
                "SELECT codigo, nombre, precio, imagen FROM productos WHERE LOWER(nombre) LIKE LOWER(%s)",
                [f'%{nombre}%']
            )
        else:
            cursor.execute("SELECT codigo, nombre, precio, imagen FROM productos")
        
        productos = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return productos
    
    @staticmethod
    def obtener_por_codigo(codigo):
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute(
            "SELECT codigo, nombre, precio, imagen FROM productos WHERE codigo = %s",
            [codigo]
        )
        
        producto = cursor.fetchone()
        cursor.close()
        conn.close()
        
        return producto 