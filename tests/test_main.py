## /tests/test_main.py
from app.services import add_task, get_task, update_task, delete_task
from app.models import Task

def test_add_task():
    task = Task(id=1, title="Test Task", description="This is a test", completed=False)
    assert add_task(task) == task

def test_get_task():
    assert get_task(1) is not None

def test_update_task():
    updated_task = Task(id=1, title="string_type", description="Updated", completed="True")
    assert update_task(1, updated_task) == updated_task

def test_delete_task():
    assert delete_task(1) == {"message": "Task deleted com sucesso!"}
