from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db
from ..auth import get_current_user

router = APIRouter(prefix="/servicios", tags=["Servicios"])


@router.post("/", response_model=schemas.ServicioResponse)
def create_servicio(servicio: schemas.ServicioCreate, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    return crud.create_servicio(db, servicio)


@router.get("/", response_model=list[schemas.ServicioResponse])
def get_servicios(db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    return crud.get_servicios(db)


@router.get("/total")
def get_servicios_total(db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    return crud.get_servicios_total(db)


@router.get("/{servicio_id}", response_model=schemas.ServicioResponse)
def get_servicio(servicio_id: int, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    return crud.get_servicio_by_id(db, servicio_id)


@router.delete("/{servicio_id}")
def delete_servicio(servicio_id: int, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    return crud.delete_servicio(db, servicio_id)