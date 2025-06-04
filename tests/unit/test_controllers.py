"""
Unit tests for controllers
"""
import pytest
from app.controllers.productos_controller import ProductosController
from app.models.producto import Producto

def test_buscar_producto_por_codigo(init_database):
    """Test búsqueda de producto por código."""
    controller = ProductosController()
    producto = controller.buscar_por_codigo("TEST001")
    
    assert producto is not None
    assert producto.codigo == "TEST001"
    assert producto.nombre == "Producto Test 1"

def test_buscar_producto_inexistente(init_database):
    """Test búsqueda de producto que no existe."""
    controller = ProductosController()
    producto = controller.buscar_por_codigo("NOEXISTE")
    
    assert producto is None

def test_listar_productos(init_database):
    """Test listado de productos."""
    controller = ProductosController()
    productos = controller.listar_productos()
    
    assert len(productos) == 2
    assert any(p.codigo == "TEST001" for p in productos)
    assert any(p.codigo == "TEST002" for p in productos)

def test_formato_respuesta_producto(init_database):
    """Test formato de respuesta de producto."""
    controller = ProductosController()
    producto = controller.buscar_por_codigo("TEST001")
    respuesta = controller.formato_respuesta(producto)
    
    assert "codigo" in respuesta
    assert "nombre" in respuesta
    assert "precio" in respuesta
    assert "imagen_url" in respuesta
    assert respuesta["codigo"] == "TEST001" 