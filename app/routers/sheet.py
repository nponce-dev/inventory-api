from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db
from ..auth import get_current_user

router = APIRouter(prefix="/sheet", tags=["Sheet"])


@router.get("/productos")
def get_sheet_productos(user: str = Depends(get_current_user)):
    return crud.get_sheet_productos()


@router.get("/mappings", response_model=list[schemas.ProductMappingResponse])
def get_mappings(db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    return crud.get_mappings(db)


@router.post("/mappings", response_model=schemas.ProductMappingResponse)
def create_mapping(mapping: schemas.ProductMappingCreate, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    return crud.create_mapping(db, mapping)


@router.delete("/mappings/{mapping_id}")
def delete_mapping(mapping_id: int, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    return crud.delete_mapping(db, mapping_id)


@router.post("/sync")
def sync_sheet(db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    return crud.sync_sheet(db)