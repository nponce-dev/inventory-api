from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db
from ..auth import get_current_user

router = APIRouter(prefix="/ventas", tags=["Ventas Carrito"])


@router.post("/", response_model=schemas.VentaResponse)
def create_venta(venta: schemas.VentaCreate, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    return crud.create_venta_carrito(db, venta)


@router.get("/", response_model=list[schemas.VentaResponse])
def get_ventas(db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    return crud.get_ventas_carrito(db)


@router.delete("/{venta_id}")
def delete_venta(venta_id: int, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    return crud.delete_venta_carrito(db, venta_id)