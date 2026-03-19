from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/sales", tags=["Sales"])


@router.post("/", response_model=schemas.SaleResponse)
def create_sale(sale: schemas.SaleCreate, db: Session = Depends(get_db)):
    return crud.make_sale(db, sale)


@router.get("/", response_model=list[schemas.SaleResponse])
def get_sales(db: Session = Depends(get_db)):
    return crud.get_sales(db)

