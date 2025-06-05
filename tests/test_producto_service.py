import unittest
from unittest.mock import patch, MagicMock
from app import create_app
from app.services.producto_service import ProductosService
from app.models.producto import Producto

class TestProductoService(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    @patch('app.models.producto.Producto.query')
    def test_listar(self, mock_query):
        # Configurar el mock para simular una lista de productos
        mock_producto = MagicMock()
        mock_producto.to_dict.return_value = {'codigo': '123', 'nombre': 'Test Product', 'precio': 10.0}
        mock_query.filter.return_value.limit.return_value.all.return_value = [mock_producto]

        # Llamar al método listar
        result = ProductosService.listar(nombre='Test', limite=10)

        # Verificar que se llamó a la consulta y que el resultado es correcto
        mock_query.filter.assert_called_once()
        self.assertEqual(result, [mock_producto])

    @patch('app.models.producto.Producto.query')
    def test_buscar_por_codigo(self, mock_query):
        # Configurar el mock para simular un producto encontrado
        mock_producto = MagicMock()
        mock_query.filter_by.return_value.first.return_value = mock_producto

        # Llamar al método buscar_por_codigo
        result = ProductosService.buscar_por_codigo('123')

        # Verificar que se llamó a la consulta y que el resultado es correcto
        mock_query.filter_by.assert_called_once_with(codigo='123')
        self.assertEqual(result, mock_producto)

if __name__ == '__main__':
    unittest.main()