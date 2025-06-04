from flask import jsonify, request
from app.models.producto import Producto

class ProductosController:

    @staticmethod
    def buscar_por_codigo(codigo):
        """Buscar un producto por su código."""
        return Producto.query.filter_by(codigo=codigo).first()

    @staticmethod
    def formato_respuesta(producto):
        """Convertir un producto a formato JSON."""
        if not producto:
            return None
        return producto.to_dict()

def obtener_productos():
    """Endpoint para obtener todos los productos."""
    controller = ProductosController()
    
    nombre = request.args.get('nombre')
    limite = request.args.get('limite', type=int)
    
    productos = controller.listar_productos(limite)
    
    if not productos:
        return "", 204
    
    response = [p.to_dict() for p in productos]
    
    return jsonify(response), 200

def obtener_producto_por_codigo(codigo):
    """Endpoint para obtener un producto por su código."""
    controller = ProductosController()
    
    producto = controller.buscar_por_codigo(codigo)
    
    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404
    
    return jsonify(controller.formato_respuesta(producto)), 200 