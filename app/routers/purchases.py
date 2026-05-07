from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/purchases", tags=["Purchases"])


@router.post("/", response_model=schemas.PurchaseResponse)
def create_purchase(purchase: schemas.PurchaseCreate, db: Session = Depends(get_db)):
    return crud.create_purchase(db, purchase)


@router.get("/", response_model=list[schemas.PurchaseResponse])
def get_purchases(db: Session = Depends(get_db)):
    return crud.get_purchases(db)


@router.get("/summary")
def get_summary(db: Session = Depends(get_db)):
    total_compras = crud.get_purchase_total(db)
    total_ventas = crud.get_sales_total(db)
    servicios_data = crud.get_servicios_total(db)
    total_servicios = servicios_data["ingresos"]
    costo_productos_servicios = servicios_data["costo_productos"]
    
    total_ingresos = total_ventas + total_servicios
    total_gastos = total_compras + costo_productos_servicios
    
    return {
        "total_compras": round(total_compras, 2),
        "total_ventas": round(total_ventas, 2),
        "total_servicios": round(total_servicios, 2),
        "costo_productos_servicios": round(costo_productos_servicios, 2),
        "total_ingresos": round(total_ingresos, 2),
        "ganancia_neta": round(total_ingresos - total_gastos, 2)
    }

@router.delete("/{purchase_id}")
def delete_purchase(purchase_id: int, db: Session = Depends(get_db)):
    return crud.delete_purchase(db, purchase_id)
