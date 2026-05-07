from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List
from datetime import datetime


# =========================
# PRODUCT
# =========================

class ProductCreate(BaseModel):
    name: str
    sku: str
    stock: int = Field(ge=0)
    precio_venta: Optional[float] = Field(default=None, ge=0)


class ProductUpdate(BaseModel):
    name: str
    sku: str
    stock: int = Field(ge=0)
    precio_venta: Optional[float] = Field(default=None, ge=0)


class ProductResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    sku: str
    stock: int
    precio_venta: Optional[float] = None


# =========================
# SALE
# =========================

class SaleCreate(BaseModel):
    sku: str
    quantity: int = Field(gt=0)
    precio_unitario_real: Optional[float] = Field(default=None, ge=0)


class SaleResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    product_id: int
    quantity: int
    precio_unitario_real: Optional[float] = None


# =========================
# PURCHASE
# =========================

class PurchaseItemCreate(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)


class PurchaseCreate(BaseModel):
    precio_total: float = Field(gt=0)
    items: List[PurchaseItemCreate]


class PurchaseItemResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    product_id: int
    quantity: int


class PurchaseResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    precio_total: float
    fecha: datetime
    items: List[PurchaseItemResponse]

class DiscountItemCreate(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)

class DiscountCreate(BaseModel):
    name: str
    precio_descuento: float = Field(gt=0)
    items: List[DiscountItemCreate]

class DiscountItemResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    product_id: int
    quantity: int

class DiscountResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    precio_descuento: float
    fecha: datetime
    items: List[DiscountItemResponse]

# =========================
# SERVICIOS
# =========================

class ServicioItemCreate(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)


class ServicioCreate(BaseModel):
    tipo: str
    cliente_nombre: str
    mascota_nombre: str
    precio_cobrado: float = Field(gt=0)
    items: List[ServicioItemCreate]


class ServicioItemResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    product_id: int
    quantity: int


class ServicioResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    tipo: str
    cliente_nombre: str
    mascota_nombre: str
    precio_cobrado: float
    fecha: Optional[datetime] = None
    items: List[ServicioItemResponse]