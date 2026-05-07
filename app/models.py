from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    sku = Column(String, nullable=False, unique=True, index=True)
    stock = Column(Integer, nullable=False, default=0)
    precio_venta = Column(Float, nullable=True, default=None)

    sales = relationship("Sale", back_populates="product")
    purchase_items = relationship("PurchaseItem", back_populates="product")


class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    precio_unitario_real = Column(Float, nullable=True, default=None)

    product = relationship("Product", back_populates="sales")


class Purchase(Base):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True, index=True)
    precio_total = Column(Float, nullable=False)
    fecha = Column(DateTime(timezone=True), server_default=func.now())

    items = relationship("PurchaseItem", back_populates="purchase")


class PurchaseItem(Base):
    __tablename__ = "purchase_items"

    id = Column(Integer, primary_key=True, index=True)
    purchase_id = Column(Integer, ForeignKey("purchases.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)

    purchase = relationship("Purchase", back_populates="items")
    product = relationship("Product", back_populates="purchase_items")

class Discount(Base):
    __tablename__ = "discounts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    precio_descuento = Column(Float, nullable=False)
    fecha = Column(DateTime(timezone=True), server_default=func.now())
    items = relationship("DiscountItem", back_populates="discount", cascade="all, delete-orphan")

class DiscountItem(Base):
    __tablename__ = "discount_items"
    id = Column(Integer, primary_key=True, index=True)
    discount_id = Column(Integer, ForeignKey("discounts.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    discount = relationship("Discount", back_populates="items")
    product = relationship("Product")

class Servicio(Base):
    __tablename__ = "servicios"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String, nullable=False)  # Clase / Guarderia / Pet Sitter
    cliente_nombre = Column(String, nullable=False)
    mascota_nombre = Column(String, nullable=False)
    precio_cobrado = Column(Float, nullable=False)
    fecha = Column(DateTime(timezone=True), server_default=func.now())

    items = relationship("ServicioItem", back_populates="servicio")


class ServicioItem(Base):
    __tablename__ = "servicio_items"

    id = Column(Integer, primary_key=True, index=True)
    servicio_id = Column(Integer, ForeignKey("servicios.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)

    servicio = relationship("Servicio", back_populates="items")
    product = relationship("Product")   