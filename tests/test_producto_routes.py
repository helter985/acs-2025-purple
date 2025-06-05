import unittest
from unittest.mock import patch, MagicMock
from app import create_app

class TestProductoRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()

    @patch('app.routes.producto_routes.ProductosService')
    def test_get_productos(self, mock_service):
        # Configurar el mock para simular una lista de productos
        mock_producto = MagicMock()
        mock_producto.to_dict.return_value = {'codigo': '123', 'nombre': 'Test Product', 'precio': 10.0}
        mock_service.listar.return_value = [mock_producto]

        # Llamar al endpoint
        response = self.client.get('/v1/productos')

        # Verificar que se llamó al servicio y que la respuesta es correcta
        mock_service.listar.assert_called_once_with(None, None)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [{'codigo': '123', 'nombre': 'Test Product', 'precio': 10.0}])

    @patch('app.routes.producto_routes.ProductosService')
    def test_get_producto(self, mock_service):
        # Configurar el mock para simular un producto encontrado
        mock_producto = MagicMock()
        mock_producto.to_dict.return_value = {'codigo': '123', 'nombre': 'Test Product', 'precio': 10.0}
        mock_service.buscar_por_codigo.return_value = mock_producto

        # Llamar al endpoint
        response = self.client.get('/v1/productos/123')

        # Verificar que se llamó al servicio y que la respuesta es correcta
        mock_service.buscar_por_codigo.assert_called_once_with('123')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'codigo': '123', 'nombre': 'Test Product', 'precio': 10.0})

    @patch('app.routes.producto_routes.ProductosService')
    def test_get_producto_not_found(self, mock_service):
        # Configurar el mock para simular que no se encuentra el producto
        mock_service.buscar_por_codigo.return_value = None

        # Llamar al endpoint
        response = self.client.get('/v1/productos/999')

        # Verificar que se llamó al servicio y que la respuesta es correcta
        mock_service.buscar_por_codigo.assert_called_once_with('999')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {'error': 'Producto no encontrado'})

if __name__ == '__main__':
    unittest.main()