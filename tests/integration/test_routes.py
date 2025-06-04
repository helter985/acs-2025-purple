"""
Integration tests for API routes
"""
import json
import pytest

def test_get_productos(client, init_database):
    """Test GET /productos."""
    response = client.get('/v1/productos')
    
    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    assert len(data) == 2
    assert all(key in data[0] for key in ['codigo', 'nombre', 'precio', 'imagen_url'])

def test_get_producto_por_codigo(client, init_database):
    """Test GET /productos/{codigo} con producto existente."""
    response = client.get('/v1/productos/TEST001')
    
    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    assert data['codigo'] == 'TEST001'
    assert data['nombre'] == 'Producto Test 1'
    assert data['precio'] == 100.50
    assert data['imagen_url'] == 'http://ejemplo.com/imagen1.jpg'

def test_get_producto_no_existente(client, init_database):
    """Test GET /productos/{codigo} con producto no existente."""
    response = client.get('/v1/productos/NOEXISTE')
    
    assert response.status_code == 404
    data = json.loads(response.data.decode('utf-8'))
    assert 'error' in data

def test_get_productos_headers(client, init_database):
    """Test headers en respuesta GET /productos."""
    response = client.get('/v1/productos')
    
    assert response.status_code == 200
    assert response.content_type == 'application/json'

def test_metodo_no_permitido(client, init_database):
    """Test método no permitido en endpoints."""
    response = client.post('/v1/productos')
    assert response.status_code == 405
    
    response = client.put('/v1/productos/TEST001')
    assert response.status_code == 405
    
    response = client.delete('/v1/productos/TEST001')
    assert response.status_code == 405

def test_formato_json_invalido(client, init_database):
    """Test manejo de formato JSON inválido."""
    response = client.get('/v1/productos/TEST001')
    data = json.loads(response.data.decode('utf-8'))
    
    assert isinstance(data['precio'], float)
    assert isinstance(data['codigo'], str)
    assert isinstance(data['nombre'], str)
    assert isinstance(data['imagen_url'], str) 