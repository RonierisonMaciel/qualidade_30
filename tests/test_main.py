from app.models import Task
from app.services import add_task, update_task, delete_task


# Teste de criação de tarefa
def test_add_task():
    task = Task(id=1, title="New Task", description="Test Task", completed=False)
    result = add_task(task)
    assert result == task


# Teste de atualização de tarefa
def test_update_task():
    updated_task = Task(
        id=1, title="Updated Title", description="Updated", completed=True
    )  # ✅ Corrigido o tipo do title (string ao invés de int)
    result = update_task(1, updated_task)
    assert result.title == "Updated Title"
    assert result.completed is True


# Teste de deleção de tarefa
def test_delete_task():
    assert delete_task(1) == {"message": "Task deleted com sucesso!"}  