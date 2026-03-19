from fastapi import FastAPI
from app.database import engine, Base
from app.routers import products, sales

app = FastAPI(title="Inventario API")

# Crear tablas
Base.metadata.create_all(bind=engine)

# Registrar routers
app.include_router(products.router)
app.include_router(sales.router)

