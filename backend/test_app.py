from fastapi.testclient import TestClient
import pytest

from main import app  # reemplaza con la forma correcta de importar tu app FastAPI

client = TestClient(app)

def test_read_cliente():
    response = client.get("/clientes/1")  # Suponiendo que tienes un cliente con ID 1 en tu BD
    assert response.status_code == 200
    assert "Nombre" in response.json()

def test_read_all_clientes():
    response = client.get("/clientes/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_factura():
    response = client.get("/facturas/1")  # Suponiendo que tienes una factura con ID 1 en tu BD
    assert response.status_code == 200
    assert "FacturaID" in response.json()

# ... y así sucesivamente para cada endpoint
