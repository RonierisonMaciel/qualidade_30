## /tests/test_api.py
from fastapi.testclient import TestClient
from app.main import app
from app.models import Task
from app.services import add_task, delete_task

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
    task = Task(id=1, title="Test Task", description="This is a test", completed=False)
    add_task(task)
    response = delete_task(1)
    assert response == {"message": "Task deleted com sucesso!"}

