from app.models.db import db
import re

class Producto(db.Model):
    __tablename__ = 'productos'
    
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(50), unique=True, nullable=False)
    nombre = db.Column(db.String(200), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    imagen_url = db.Column(db.String(255))

    def __init__(self, codigo, nombre, precio, imagen_url=None):
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        if not codigo:
            raise ValueError("El código es requerido")
        if not nombre:
            raise ValueError("El nombre es requerido")
        if imagen_url and not self._es_url_valida(imagen_url):
            raise ValueError("La URL de la imagen no es válida")
            
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.imagen_url = imagen_url

    def __repr__(self):
        return f"{self.nombre} ({self.codigo})"

    def to_dict(self):
        return {
            'codigo': self.codigo,
            'nombre': self.nombre,
            'precio': self.precio,
            'imagen_url': self.imagen_url
        }
