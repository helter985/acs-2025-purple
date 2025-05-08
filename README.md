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
- **Vendedor:**  
  Usuario final que consulta la lista de precios a través de un dispositivo móvil.

- **Administrador del Sistema:**  
  Encargado de la carga y gestión de las imágenes de los productos y del mantenimiento de la API de actualización. Además, responsable de actualizar y normalizar las listas de precios recibidas de los proveedores, garantizando la disponibilidad de la última versión.

---

## 2. Requerimientos

### 2.1 Descripción de Roles
- **Vendedor:**  
  Consulta el precio de venta de cada artículo usando su dispositivo móvil. Su interacción se limita a la visualización de datos (imagen, nombre, precio y código).

- **Administrador del Sistema:**  
  Se encarga de integrar las imágenes de los productos en el sistema, ya que estas no vienen en las listas de precios y deben cargarse manualmente. Además, actualiza la base de datos de precios (normalizando las distintas listas de proveedores) y se encarga de ejecutar las actualizaciones, que se realizan entre una y dos veces por semana.

### 2.2 Features por Rol

#### Vendedor
- **Consulta de Precios:**  
  - Visualización de la imagen, nombre, precio y código de producto.
  - Interfaz de usuario sencilla que no requiere capacitación.
- **Dispositivos:**  
  - La aplicación estará optimizada para celulares con sistemas Android e iOS.

#### Administrador del Sistema
- **Carga de Imágenes:**  
  - Integración de imágenes para cada producto.
- **Mantenimiento del API:**  
  - Desarrollo o integración de una API que permita la actualización en tiempo real de los precios.
- **Actualización y Normalización de Listas:**  
  - Actualización de listas (1-2 veces por semana) con sincronización en tiempo real.
  - Gestión de versiones para asegurar que solo se visualice la última lista de precios.

### 2.3 User Stories

#### Vendedor

- **US01**
  > Como vendedor, quiero poder consultar el precio de un producto escaneando su código de barras o ingresando su código interno, para obtener rápidamente su precio, nombre e imagen.

- **US02**
  > Como vendedor, quiero ver claramente el nombre, precio, imagen y código del producto en pantalla, para tomar decisiones informadas al momento de vender.

- **US03**
  > Como vendedor, quiero que la interfaz de la aplicación sea intuitiva y simple, para poder usarla sin capacitación previa.

- **US04**
  > Como vendedor, quiero poder usar la aplicación en mi dispositivo móvil Android o iOS, para consultarla desde cualquier lugar.

#### Administrador del Sistema

- **US05**
  > Como administrador, quiero poder cargar manualmente las imágenes de los productos, para que los vendedores las vean junto con los precios.

- **US06**
  > Como administrador, quiero mantener y configurar una API para actualizar los precios en tiempo real, para que la aplicación siempre muestre la lista más reciente.

- **US07**
  > Como administrador, quiero poder subir y normalizar las listas de precios de los proveedores 1-2 veces por semana, para garantizar que la información esté actualizada y unificada.

- **US08**
  > Como administrador, quiero asegurarme de que la aplicación solo muestre la versión más reciente de la lista de precios, para evitar errores y confusiones en la venta.

### 2.4 Test Cases

#### Vendedor

- **TC01 - Consulta por código de barras o código interno (US01)**  
  **Objetivo:** Verificar que el usuario puede consultar un producto ingresando su código interno o escaneando su código de barras.  
  **Precondición:** La aplicación está instalada y en funcionamiento.  
  **Pasos:**
  1. Ingresar o escanear el código de un producto válido.
  2. Presionar el botón de búsqueda.
  **Resultado esperado:** Se muestra el producto con su imagen, nombre, precio y código.

- **TC02 - Visualización de datos del producto (US02)**  
  **Objetivo:** Verificar que la información del producto se muestre de forma clara y completa.  
  **Precondición:** El producto fue buscado correctamente.  
  **Pasos:**
  1. Consultar un producto existente.
  **Resultado esperado:** La pantalla muestra correctamente la imagen, nombre, código y precio del producto.

- **TC03 - Facilidad de uso de la interfaz (US03)**  
  **Objetivo:** Evaluar que la interfaz sea intuitiva para nuevos usuarios.  
  **Precondición:** Usuario sin experiencia previa accede a la aplicación.  
  **Pasos:**
  1. Abrir la aplicación.
  2. Intentar realizar una búsqueda sin instrucciones previas.
  **Resultado esperado:** El usuario puede realizar la búsqueda sin asistencia externa.

- **TC04 - Compatibilidad con Android e iOS (US04)**  
  **Objetivo:** Verificar que la aplicación funcione correctamente en dispositivos Android e iOS.  
  **Precondición:** Dispositivos con ambos sistemas operativos disponibles.  
  **Pasos:**
  1. Instalar y abrir la app en Android.
  2. Repetir en iOS.
  3. Realizar una búsqueda en ambas plataformas.
  **Resultado esperado:** Funcionalidad completa y sin errores en ambos sistemas.

#### Administrador del Sistema

- **TC05 - Carga manual de imágenes (US05)**  
  **Objetivo:** Verificar que el administrador pueda cargar imágenes para los productos.  
  **Precondición:** Acceso de administrador y producto existente sin imagen.  
  **Pasos:**
  1. Ingresar al panel de administración.
  2. Seleccionar un producto.
  3. Subir una imagen y guardarla.
  **Resultado esperado:** La imagen se guarda correctamente y es visible en la app.

- **TC06 - Funcionamiento de la API de actualización (US06)**  
  **Objetivo:** Verificar que la API permita actualizar los precios en tiempo real.  
  **Precondición:** La API está configurada y en línea.  
  **Pasos:**
  1. Realizar una modificación de precio desde la fuente.
  2. Ejecutar el proceso de actualización.
  **Resultado esperado:** El nuevo precio se refleja en la app inmediatamente.

- **TC07 - Subida y normalización de listas (US07)**  
  **Objetivo:** Comprobar que se pueden subir nuevas listas y se normalicen correctamente.  
  **Precondición:** Archivo de lista de precios de proveedor disponible.  
  **Pasos:**
  1. Subir la nueva lista desde el panel.
  2. Ejecutar proceso de normalización.
  **Resultado esperado:** La lista se incorpora al sistema con los datos correctamente formateados.

- **TC08 - Visualización de la última versión (US08)**  
  **Objetivo:** Verificar que la app solo muestre la última versión de la lista de precios.  
  **Precondición:** Se suben varias versiones de una misma lista.  
  **Pasos:**
  1. Subir una lista antigua.
  2. Subir una nueva versión.
  3. Consultar precios desde la app.
  **Resultado esperado:** Solo la última versión está visible para los usuarios.

## 3.2 - Definición de API

La API fue definida utilizando OpenAPI 3.0 y permite realizar las siguientes operaciones:

### Endpoints

- `GET /productos`  
- `GET /productos/{codigo}`  

### Contrato OpenAPI

📄 Archivo disponible en: [`openapi.yaml`](openapi.yaml)

---
