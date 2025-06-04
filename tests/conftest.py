"""
Fixtures for testing the API de Consulta de Lista de Precios
"""
import pytest
from app import create_app
from app.models.db import db
from app.models.producto import Producto

@pytest.fixture
def app():
    """Create application for the tests."""
    test_app = create_app()
    test_app.config['TESTING'] = True
    test_app.config['JSON_AS_ASCII'] = False
    
    return test_app

@pytest.fixture
def client(app):
    """Create test client."""
    return app.test_client()

@pytest.fixture
def init_database(app):
    """Initialize test database."""
    with app.app_context():
        # Limpiar los datos de prueba antes de cada test
        db.session.query(Producto).delete()
        
        producto1 = Producto(
            codigo="TEST001",
            nombre="Producto Test 1",
            precio=100.50,
            imagen_url="http://ejemplo.com/imagen1.jpg"
        )
        producto2 = Producto(
            codigo="TEST002",
            nombre="Producto Test 2",
            precio=200.75,
            imagen_url="http://ejemplo.com/imagen2.jpg"
        )
        
        db.session.add(producto1)
        db.session.add(producto2)
        db.session.commit()

        yield db
        
        # Limpiar los datos de prueba después de cada test
        db.session.query(Producto).delete()
        db.session.commit()
        db.session.remove() 