from app.services import add_task, get_task, update_task_in_db, delete_task
from app.models import Task

def test_add_task():
    task = Task(id=1, title="Test Task", description="This is a test", completed=False)
    assert add_task(task) == task

def test_get_task():
    task = Task(id=1, title="Test Task", description="This is a test", completed=False)
    add_task(task)
    assert get_task(1) is not None

def test_update_task():
   
    task = Task(id=1, title="Test Task", description="This is a test", completed=False)
    add_task(task)
    updated_task = Task(id=1, title="Updated Task", description="Updated", completed=True)
    updated = update_task_in_db(1, updated_task)  
    assert updated == updated_task

def test_delete_task():
    
    task = Task(id=1, title="Test Task", description="This is a test", completed=False)
    add_task(task)
    result = delete_task(1)
    assert result == {"message": "Task deleted com sucesso!"}

