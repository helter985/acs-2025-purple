# Test Plan - Consulta de Lista de Precios - Purple
# Requisitos

* Python 3.11+
* PostgreSQL (con base de datos creada previamente)
* pgAdmin 4 (opcional para administración visual)

---

## Instalación

1. **Clonar el repositorio**

```bash
git clone https://github.com/helter985/acs-2025-purple.git
cd acs-2025-purple
```

2. **Crear y activar el entorno virtual**

```bash
python -m venv venv
venv\Scripts\activate  # En Linux/macOS: source venv/bin/activate
```

3. **Instalar dependencias**

```bash
pip install -r requirements.txt
```

4. **Configurar variables de entorno**

Copiar el archivo `.env.example` y renombrarlo como `.env`:

```bash
copy .env_example .env  # En Linux/macOS: cp .env_example .env
```

Luego completar las variables necesarias en `.env` según el entorno


4. **Ejecutar la aplicación**

```bash
python app.py
```

5. **(Opcional) Ejecutar los tests**

```bash
python -m unittest discover -s tests
```

---

## Estructura del Proyecto

```
acs-2025-purple/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models/
│   ├── routes/
│   ├── services/
│   └── tests/
│       ├── __init__.py
│       ├── test_producto_routes.py
│       └── test_producto_service.py
├── venv/
├── .env.example
├── .gitignore
├── ADMIN_MVC.md
├── app.py
├── init_db.py
├── openapi.yaml
├── README.md
└── requirements.txt
```

## 1. Introducción

### 1.1 Propósito

Este documento define el plan de pruebas para la API de Consulta de Lista de Precios, diseñada para que los vendedores de una distribuidora de artículos de limpieza puedan consultar de forma rápida y precisa el precio de venta de un producto desde una aplicación móvil. La API expone la información de productos y precios de manera segura y actualizada.

### 1.2 Alcance de las Pruebas

**En Alcance (In Scope):**
- Consulta de precios mediante código de barras o código interno a través de la API.
- Sincronización en tiempo real para mostrar la última versión de la lista.
- Visualización de la imagen, nombre, precio y código de cada producto.
- Compatibilidad de la API con dispositivos móviles Android e iOS.
- Performance y respuesta adecuada de la API.

**Fuera de Alcance (Out of Scope):**
- Control de stock.
- Seguridad avanzada (protección de la integridad de la información).
- Gestión de pedidos.
- Carga, actualización y normalización de listas de precios (estas funcionalidades corresponden al panel de administración y se documentan por separado).

### 1.3 Definiciones y Roles

- **Vendedor:**  Usuario final que consulta la lista de precios a través de una aplicación móvil que consume la API de solo lectura.

> **Nota:**
> Todas las funcionalidades relacionadas con la administración, carga y normalización de listas de precios, así como la gestión de imágenes, corresponden al panel MVC y se documentan en un archivo aparte (`ADMIN_MVC.md`).

---

## 2. Requerimientos

### 2.1 Descripción de Rol

- **Vendedor:**  Consulta el precio de venta de cada artículo usando su dispositivo móvil. Su interacción se limita a la visualización de datos (imagen, nombre, precio y código) a través de la API.

### 2.2 User Stories

- **US01**
  > Como vendedor, quiero poder consultar el precio de un producto escaneando su código de barras o ingresando su código interno, para obtener rápidamente su precio, nombre e imagen.

- **US02**
  > Como vendedor, quiero ver claramente el nombre, precio, imagen y código del producto en pantalla, para tomar decisiones informadas al momento de vender.

- **US03**
  > Como vendedor, quiero que la interfaz de la aplicación sea intuitiva y simple, para poder usarla sin capacitación previa.

- **US04**
  > Como vendedor, quiero poder usar la aplicación en mi dispositivo móvil Android o iOS, para consultarla desde cualquier lugar.

### 2.3 Test Cases

- **TC01 - Consulta por código de barras o código interno (US01)**  
  **Objetivo:** Verificar que el usuario puede consultar un producto ingresando su código interno o escaneando su código de barras a través de la API.  
  **Precondición:** La aplicación móvil está instalada y en funcionamiento.  
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
  **Objetivo:** Verificar que la aplicación funcione correctamente en dispositivos Android e iOS usando la API.  
  **Precondición:** Dispositivos con ambos sistemas operativos disponibles.  
  **Pasos:**
  1. Instalar y abrir la app en Android.
  2. Repetir en iOS.
  3. Realizar una búsqueda en ambas plataformas.
  **Resultado esperado:** Funcionalidad completa y sin errores en ambos sistemas.

---

## 3. Especificaciones

### 3.1 Arquitectura

La arquitectura del sistema responde a un modelo **cliente-servidor**. La API RESTful expone endpoints de solo lectura para que los vendedores consulten productos y precios en tiempo real desde la aplicación móvil.

#### Componentes principales

- **API RESTful (solo lectura)**  
  Intermediaria entre el backend y los clientes móviles.  
  - Expone **endpoints seguros y de solo lectura** que permiten a los vendedores consultar productos y precios en tiempo real.
  - **No permite la carga ni modificación de datos.**

- **Base de datos**  
  Contiene los productos, precios y referencias a imágenes.  
  - Es accedida por la API para exponer la información a los vendedores.

- **Aplicación del Vendedor**  
  Interfaz móvil sencilla que permite al vendedor acceder a la información de productos.  
  - Se conecta exclusivamente a través de la API para obtener datos actualizados.

> **Nota:**
> El panel de administración (MVC) y todas las funcionalidades de carga y mantenimiento de datos se documentan en el archivo `ADMIN_MVC.md`.

![Diagrama de Arquitectura](https://lucid.app/publicSegments/view/edc0d672-c7c9-4298-bd47-8efb37299654/image.png)

## 3.2 - Definición de API

La API fue definida utilizando OpenAPI 3.0 y permite realizar las siguientes operaciones de solo lectura:

### Endpoints

- `GET /productos`  
- `GET /productos/{codigo}`  

### Contrato OpenAPI

📄 Archivo disponible en: [`openapi.yaml`](openapi.yaml)

> **Nota:** La API es utilizada únicamente por la aplicación móvil de los vendedores para consultar información.  
> La carga y actualización de datos se realiza exclusivamente desde el panel de administración (MVC), documentado en `ADMIN_MVC.md`.

---