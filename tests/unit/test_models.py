"""
Unit tests for models
"""
import pytest
from app.models.producto import Producto

def test_nuevo_producto():
    """Test creación de nuevo producto."""
    producto = Producto(
        codigo="TEST003",
        nombre="Producto Test 3",
        precio=150.75,
        imagen_url="http://ejemplo.com/imagen3.jpg"
    )
    
    assert producto.codigo == "TEST003"
    assert producto.nombre == "Producto Test 3"
    assert producto.precio == 150.75
    assert producto.imagen_url == "http://ejemplo.com/imagen3.jpg"

def test_producto_precio_invalido():
    """Test validación de precio negativo."""
    with pytest.raises(ValueError):
        Producto(
            codigo="TEST004",
            nombre="Producto Test 4",
            precio=-100,
            imagen_url="http://ejemplo.com/imagen4.jpg"
        )

def test_producto_codigo_requerido():
    """Test código requerido."""
    with pytest.raises(ValueError):
        Producto(
            codigo=None,
            nombre="Producto Test 5",
            precio=100,
            imagen_url="http://ejemplo.com/imagen5.jpg"
        )

def test_producto_nombre_requerido():
    """Test nombre requerido."""
    with pytest.raises(ValueError):
        Producto(
            codigo="TEST005",
            nombre=None,
            precio=100,
            imagen_url="http://ejemplo.com/imagen5.jpg"
        )

def test_producto_imagen_url_formato():
    """Test formato URL de imagen."""
    with pytest.raises(ValueError):
        Producto(
            codigo="TEST006",
            nombre="Producto Test 6",
            precio=100,
            imagen_url="url_invalida"
        )

def test_producto_representacion():
    """Test representación string del producto."""
    producto = Producto(
        codigo="TEST007",
        nombre="Producto Test 7",
        precio=175.50,
        imagen_url="http://ejemplo.com/imagen7.jpg"
    )
    
    assert str(producto) == "Producto Test 7 (TEST007)" 