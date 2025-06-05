from app.models.producto import Producto

class ProductosService:
    @staticmethod
    def listar(nombre=None, limite=None):
        """Listar productos opcionalmente filtrados por nombre y con un límite."""
        query = Producto.query
        if nombre:
            query = query.filter(Producto.nombre.ilike(f'%{nombre}%'))
        if limite:
            query = query.limit(limite)
        return query.all()

    @staticmethod
    def buscar_por_codigo(codigo):
        """Buscar un producto por su código."""
        return Producto.query.filter_by(codigo=codigo).first() 