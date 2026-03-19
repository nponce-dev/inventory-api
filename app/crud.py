from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas


# =========================
# PRODUCTOS
# =========================

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_products(db: Session):
    return db.query(models.Product).all()


def get_product_by_id(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()


def update_product(db: Session, product_id: int, product: schemas.ProductUpdate):
    db_product = get_product_by_id(db, product_id)
    if not db_product:
        return None

    for key, value in product.model_dump().items():
        setattr(db_product, key, value)

    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: int):
    db_product = get_product_by_id(db, product_id)
    if not db_product:
        return None

    db.delete(db_product)
    db.commit()
    return True


# =========================
# VENTAS
# =========================

def make_sale(db: Session, sale: schemas.SaleCreate):
    product = db.query(models.Product).filter(models.Product.sku == sale.sku).first()

    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    if product.stock < sale.quantity:
        raise HTTPException(status_code=400, detail="Stock insuficiente")

    product.stock -= sale.quantity

    db_sale = models.Sale(product_id=product.id, quantity=sale.quantity)
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)

    return db_sale


def get_sales(db: Session):
    return db.query(models.Sale).all()
