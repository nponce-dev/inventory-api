from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import HTTPException

from app.database import engine, Base
from app.routers import products, sales, purchases, discounts
from app.auth import USERS, verify_password, create_token, get_current_user

app = FastAPI(title="Inventario API")

Base.metadata.create_all(bind=engine, checkfirst=True)

# Agregar columnas nuevas si no existen (PostgreSQL)
from sqlalchemy import text, inspect
with engine.connect() as conn:
    inspector = inspect(engine)
    columnas = [c['name'] for c in inspector.get_columns('sales')]
    if 'precio_unitario_real' not in columnas:
        conn.execute(text("ALTER TABLE sales ADD COLUMN precio_unitario_real FLOAT"))
        conn.commit()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/token")
def login(form: OAuth2PasswordRequestForm = Depends()):
    user = USERS.get(form.username)
    if not user or not verify_password(form.password, user["password"]):
        raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")
    token = create_token({"sub": form.username})
    return {"access_token": token, "token_type": "bearer"}

app.include_router(products.router, dependencies=[Depends(get_current_user)])
app.include_router(sales.router, dependencies=[Depends(get_current_user)])
app.include_router(purchases.router, dependencies=[Depends(get_current_user)])
app.include_router(discounts.router, dependencies=[Depends(get_current_user)])
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
def serve_frontend():
    return FileResponse("frontend/index.html")
