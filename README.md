# Test Plan - Consulta de Lista de Precios - Purple

## 1. Introducción

### 1.1 Propósito

Este documento tiene como objetivo definir el plan de pruebas para la solución de Consulta de Lista de Precios, diseñada para que los vendedores de una distribuidora de artículos de limpieza puedan consultar de forma rápida y precisa el precio de venta de un producto. La solución deberá gestionar la normalización de listas de precios de distintos proveedores, garantizando la visualización de la última versión y la integración de imágenes para cada producto.

### 1.2 Scope de las Pruebas

**En Alcance (In Scope):**

- **Funcionalidad:**

  - Consulta de precios mediante código de barras o código interno.
  - Sincronización en tiempo real para mostrar la última versión de la lista.
  - Actualización de datos (ejecutada 1-2 veces por semana por el encargado de ventas).
  - Carga de imagen de cada producto.

- **Usabilidad:**

  - Interfaz intuitiva y sencilla para vendedores sin necesidad de capacitación.

- **Seguridad:**

  - Acceso público para visualización de datos.

- **Compatibilidad:**

  - Ejecución correcta en dispositivos móviles Android e iOS.

- **Performance:**

  - Respuesta adecuada en la consulta y sincronización de precios.

- **UI:**

  - Visualización correcta de la imagen, nombre, precio y código de cada producto.

- **Hardware:**

  - Verificación en dispositivos móviles utilizados por los vendedores.

**Fuera de Alcance (Out of Scope):**

- Control de stock (la aplicación solo muestra precios y no gestiona inventario).
- Seguridad (protección de la integridad de la información).
- Gestión de pedidos (funcionalidad prevista para una futura aplicación complementaria).

### 1.3 Definiciones y Roles

- **Vendedor:**\
  Usuario final que consulta la lista de precios a través de un dispositivo móvil.

- **Encargado de Ventas:**\
  Responsable de actualizar y normalizar las listas de precios recibidas de los proveedores, garantizando la disponibilidad de la última versión.

- **Proveedor:**\
  Entidad que suministra las listas de precios, en su mayoría en formato Excel, con variaciones de formato.

- **Administrador del Sistema:**\
  Encargado de la carga y gestión de las imágenes de los productos y del mantenimiento de la API de actualización.