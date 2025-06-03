from app.models.db import db

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
    def obtener_todos(nombre=None):
        query = Producto.query
        if nombre:
            query = query.filter(Producto.nombre.ilike(f'%{nombre}%'))
        return query.all()
    
    @staticmethod
    def obtener_por_codigo(codigo):
        return Producto.query.filter_by(codigo=codigo).first() 