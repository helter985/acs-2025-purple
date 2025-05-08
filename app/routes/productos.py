from flask import Blueprint
from app.controllers.productos_controller import obtener_productos, obtener_producto_por_codigo

productos_bp = Blueprint('productos', __name__)

@productos_bp.route('/productos', methods=['GET'])
def get_productos():
    return obtener_productos()

@productos_bp.route('/productos/<string:codigo>', methods=['GET'])
def get_producto(codigo):
    return obtener_producto_por_codigo(codigo) 