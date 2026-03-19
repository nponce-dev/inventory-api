from pydantic import BaseModel, Field, ConfigDict


# =========================
# PRODUCT
# =========================

class ProductCreate(BaseModel):
    name: str
    sku: str
    stock: int = Field(ge=0)


class ProductUpdate(BaseModel):
    name: str
    sku: str
    stock: int = Field(ge=0)


class ProductResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    sku: str
    stock: int


# =========================
# SALE
# =========================

class SaleCreate(BaseModel):
    sku: str
    quantity: int = Field(gt=0)


class SaleResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    product_id: int
    quantity: int