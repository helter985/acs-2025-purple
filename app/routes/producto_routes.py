from flask import Blueprint, request, jsonify
from app.services.producto_service import ProductosService

productos_bp = Blueprint('productos', __name__)

@productos_bp.route('/productos', methods=['GET'])
def get_productos():
    nombre = request.args.get('nombre')
    limite = request.args.get('limite', type=int)
    productos = ProductosService.listar(nombre, limite)
    if not productos:
        return '', 204
    return jsonify([p.to_dict() for p in productos]), 200

@productos_bp.route('/productos/<string:codigo>', methods=['GET'])
def get_producto(codigo):
    producto = ProductosService.buscar_por_codigo(codigo)
    if not producto:
        return jsonify({'error': 'Producto no encontrado'}), 404
    return jsonify(producto.to_dict()), 200