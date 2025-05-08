from flask import jsonify, request
from app.models.producto import Producto

def obtener_productos():
    # Obtener parámetro de consulta 'nombre' si existe
    nombre = request.args.get('nombre')
    
    # Obtener productos de la base de datos
    productos = Producto.obtener_todos(nombre)
    
    # Si no hay productos, devolver 204
    if not productos:
        return "", 204
    
    # Devolver la lista de productos
    return jsonify(productos), 200

def obtener_producto_por_codigo(codigo):
    # Buscar producto en la base de datos
    producto = Producto.obtener_por_codigo(codigo)
    
    # Si no se encuentra el producto, devolver 404
    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404
    
    # Devolver el producto encontrado
    return jsonify(producto), 200 