from fastapi.testclient import TestClient
from app.main import app
import uuid

client = TestClient(app)


def test_create_product():
    sku = str(uuid.uuid4())

    response = client.post("/products/", json={
        "name": "Producto test",
        "sku": sku,
        "stock": 10
    })

    assert response.status_code == 200
    data = response.json()

    assert data["name"] == "Producto test"
    assert data["sku"] == sku
    assert data["stock"] == 10

