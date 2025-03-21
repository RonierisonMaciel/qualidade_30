# tests/test_main.py

from fastapi.testclient import TestClient
from app.main import app
from app.models import Task

client = TestClient(app)

def test_create_task():
    response = client.post("/tasks", json={"id": 1, "title": "Task 1", "description": "First task", "completed": False})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "title": "Task 1", "description": "First task", "completed": False}

def test_list_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_update_task():
    updated_task = {"id": 1, "title": "Updated Title", "description": "Updated", "completed": True}  # Corrigido para string
    response = client.put("/tasks/1", json=updated_task)
    assert response.status_code == 200
    assert response.json() == updated_task

def test_delete_task():
    response = client.delete("/tasks/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Task deleted com sucesso"}
