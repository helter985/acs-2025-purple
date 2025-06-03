# Documentación del Panel de Administración (MVC) - Consulta de Lista de Precios - Purple

## 1. Introducción

Este documento describe las funcionalidades, requerimientos y casos de prueba relacionados con el panel de administración (MVC) del sistema de Consulta de Lista de Precios. El panel es utilizado exclusivamente por el administrador del sistema para la carga, actualización y normalización de listas de precios, así como la gestión de imágenes de productos.

## 2. Roles y Acceso

- **Administrador del Sistema:**
  - Accede al panel de administración desde una PC con una IP permitida.
  - No utiliza la API para cargar ni modificar datos.
  - Es responsable de mantener actualizada la base de datos de productos y precios.

## 3. Funcionalidades del Panel MVC

- **Carga de Imágenes:**
  - Integración de imágenes para cada producto desde el panel MVC.
- **Mantenimiento del sistema:**
  - Actualización y normalización de listas de precios de proveedores (1-2 veces por semana) desde el panel MVC.
  - Gestión de versiones para asegurar que solo se visualice la última lista de precios.
- **Restricción de acceso:**
  - El panel de administración solo es accesible desde una PC con una IP permitida.

## 4. User Stories del Administrador

- **US05**
  > Como administrador, quiero poder cargar manualmente las imágenes de los productos desde el panel MVC, para que los vendedores las vean junto con los precios.

- **US06**
  > Como administrador, quiero mantener y configurar el sistema de actualización de precios desde el panel MVC, para que la aplicación siempre muestre la lista más reciente.

- **US07**
  > Como administrador, quiero poder subir y normalizar las listas de precios de los proveedores 1-2 veces por semana desde el panel MVC, para garantizar que la información esté actualizada y unificada.

- **US08**
  > Como administrador, quiero asegurarme de que la aplicación solo muestre la versión más reciente de la lista de precios, para evitar errores y confusiones en la venta.

## 5. Casos de Prueba del Administrador

- **TC05 - Carga manual de imágenes (US05)**  
  **Objetivo:** Verificar que el administrador pueda cargar imágenes para los productos desde el panel MVC.  
  **Precondición:** Acceso de administrador (desde la IP permitida) y producto existente sin imagen.  
  **Pasos:**
  1. Ingresar al panel de administración.
  2. Seleccionar un producto.
  3. Subir una imagen y guardarla.
  **Resultado esperado:** La imagen se guarda correctamente y es visible en la app.

- **TC06 - Funcionamiento del sistema de actualización (US06)**  
  **Objetivo:** Verificar que el sistema permita actualizar los precios en tiempo real desde el panel MVC.  
  **Precondición:** El panel está accesible y en línea.  
  **Pasos:**
  1. Realizar una modificación de precio desde el panel.
  2. Ejecutar el proceso de actualización.
  **Resultado esperado:** El nuevo precio se refleja en la app inmediatamente.

- **TC07 - Subida y normalización de listas (US07)**  
  **Objetivo:** Comprobar que se pueden subir nuevas listas y se normalicen correctamente desde el panel MVC.  
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

---

Para más detalles sobre la arquitectura general y la API de consulta, consultar el archivo `README.md`. 