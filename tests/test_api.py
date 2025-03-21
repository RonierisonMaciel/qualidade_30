## /tests/test_api.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_task():
    response = client.post("/tasks", json={"id": 1, "title": "Test", "description": "Testing", "completed": False})
    assert response.status_code == 200

def test_list_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200

def test_read_task():
    response = client.get("/tasks/1")
    assert response.status_code == 200

def test_update_task():
    response = client.put("/tasks/1", json={"id": 1, "title": "Updated", "description": "Updated desc", "completed": True})
    assert response.status_code == 200

def test_delete_task():
    response = client.delete("/tasks/1")
    assert response.status_code == 200