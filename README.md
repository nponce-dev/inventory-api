📦 Inventory Management API

Español abajo

A REST API built with FastAPI and SQLAlchemy to manage product stock and sales for small businesses. Designed as a backend portfolio project with clean architecture, input validation, and automated tests.

🛠️ Tech Stack

Python 3.10+
FastAPI — modern, high-performance web framework
SQLAlchemy — ORM for database management
SQLite — lightweight local database
Pydantic v2 — data validation and serialization
Pytest — automated testing


📁 Project Structure
inventario/
├── app/
│   ├── main.py          # App entry point, router registration
│   ├── models.py        # SQLAlchemy database models
│   ├── schemas.py       # Pydantic schemas with validation
│   ├── crud.py          # Database operations layer
│   ├── database.py      # DB connection and session management
│   └── routers/
│       ├── products.py  # Product endpoints
│       └── sales.py     # Sales endpoints
└── tests/
    ├── test_products.py
    └── test_sales.py

🚀 Getting Started
1. Clone the repository
bashgit clone https://github.com/your-username/inventory-api.git
cd inventory-api
2. Install dependencies
bashpip install fastapi sqlalchemy uvicorn httpx pytest pydantic
3. Run the server
bashuvicorn app.main:app --reload

On Windows with Python from the Microsoft Store, use py -m uvicorn app.main:app --reload

4. Open the interactive docs
http://127.0.0.1:8000/docs

🔌 API Endpoints
Products
MethodEndpointDescriptionPOST/products/Create a new productGET/products/List all productsPUT/products/{id}Update a productDELETE/products/{id}Delete a product
Sales
MethodEndpointDescriptionPOST/sales/Register a sale (reduces stock automatically)GET/sales/List all sales

✅ Running Tests
bashpytest tests/ -v
Expected output:
tests/test_products.py::test_create_product        PASSED
tests/test_sales.py::test_sale_success             PASSED
tests/test_sales.py::test_sale_insufficient_stock  PASSED
tests/test_sales.py::test_sale_product_not_found   PASSED

4 passed in ~1s

🔍 Key Features

Layered architecture: models / schemas / crud / routers separation
Input validation: stock and quantity constraints enforced at the schema level
Descriptive HTTP errors: 404 for missing products, 400 for insufficient stock
Automatic stock update: each sale reduces product stock in real time
Automated tests: edge cases covered with unique SKUs per test run



📦 API de Gestión de Inventario
Una API REST construida con FastAPI y SQLAlchemy para gestionar el stock de productos y las ventas de pequeños negocios. Desarrollada como proyecto de portfolio backend con arquitectura limpia, validación de datos y tests automatizados.

🛠️ Tecnologías utilizadas

Python 3.10+
FastAPI — framework web moderno y de alto rendimiento
SQLAlchemy — ORM para gestión de base de datos
SQLite — base de datos local liviana
Pydantic v2 — validación y serialización de datos
Pytest — testing automatizado


📁 Estructura del proyecto
inventario/
├── app/
│   ├── main.py          # Punto de entrada, registro de routers
│   ├── models.py        # Modelos de base de datos con SQLAlchemy
│   ├── schemas.py       # Schemas Pydantic con validaciones
│   ├── crud.py          # Capa de operaciones con la base de datos
│   ├── database.py      # Conexión y manejo de sesiones
│   └── routers/
│       ├── products.py  # Endpoints de productos
│       └── sales.py     # Endpoints de ventas
└── tests/
    ├── test_products.py
    └── test_sales.py

🚀 Cómo correrlo
1. Clonar el repositorio
bashgit clone https://github.com/tu-usuario/inventory-api.git
cd inventory-api
2. Instalar dependencias
bashpip install fastapi sqlalchemy uvicorn httpx pytest pydantic
3. Iniciar el servidor
bashuvicorn app.main:app --reload

En Windows con Python de la Microsoft Store, usá: py -m uvicorn app.main:app --reload

4. Abrir la documentación interactiva
http://127.0.0.1:8000/docs

🔌 Endpoints disponibles
Productos
MétodoEndpointDescripciónPOST/products/Crear un nuevo productoGET/products/Listar todos los productosPUT/products/{id}Actualizar un productoDELETE/products/{id}Eliminar un producto
Ventas
MétodoEndpointDescripciónPOST/sales/Registrar una venta (descuenta stock automáticamente)GET/sales/Listar todas las ventas

✅ Correr los tests
bashpytest tests/ -v
Resultado esperado:
tests/test_products.py::test_create_product        PASSED
tests/test_sales.py::test_sale_success             PASSED
tests/test_sales.py::test_sale_insufficient_stock  PASSED
tests/test_sales.py::test_sale_product_not_found   PASSED

4 passed en ~1s