from fastapi.testclient import TestClient
from app.main import app
import uuid

client = TestClient(app)


def test_sale_success():
    sku = str(uuid.uuid4())

    client.post("/products/", json={
        "name": "Producto venta",
        "sku": sku,
        "stock": 10
    })

    response = client.post("/sales/", json={
        "sku": sku,
        "quantity": 2
    })

    assert response.status_code == 200
    data = response.json()
    assert data["quantity"] == 2


def test_sale_insufficient_stock():
    sku = str(uuid.uuid4())

    client.post("/products/", json={
        "name": "Producto limitado",
        "sku": sku,
        "stock": 5
    })

    response = client.post("/sales/", json={
        "sku": sku,
        "quantity": 100
    })

    assert response.status_code == 400
    assert response.json()["detail"] == "Stock insuficiente"


def test_sale_product_not_found():
    sku = str(uuid.uuid4())

    response = client.post("/sales/", json={
        "sku": sku,
        "quantity": 1
    })

    assert response.status_code == 404
    assert response.json()["detail"] == "Producto no encontrado"

