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

    @staticmethod
    def _es_url_valida(url):
        """Validar que la URL tenga un formato válido."""
        patron_url = re.compile(
            r'^https?://'  # http:// o https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # dominio
            r'localhost|'  # localhost
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # IP
            r'(?::\d+)?'  # puerto opcional
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return bool(patron_url.match(url))

    @staticmethod
    def obtener_todos(nombre=None):
        query = Producto.query
        if nombre:
            query = query.filter(Producto.nombre.ilike(f'%{nombre}%'))
        return query.all()
    
    @staticmethod
    def obtener_por_codigo(codigo):
        return Producto.query.filter_by(codigo=codigo).first() 