# app/services.py

from app.database import tasks
from app.models import Task

def get_task(task_id: int):
    return next((task for task in tasks if task.id == task_id), None)

def add_task(task: Task):
    tasks.append(task)
    return task

def update_task(task_id: int, updated_task: Task):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            tasks[i] = updated_task  # Atualiza a tarefa na lista
            return updated_task  # Retorna a tarefa atualizada
    return None  # Retorna None se a tarefa não for encontrada

def delete_task(task_id: int):
    # Verifica se a tarefa existe antes de tentar deletá-la
    task = get_task(task_id)
    if task:
        global tasks
        tasks = [task for task in tasks if task.id != task_id]  # Remove a tarefa da lista
        return {"message": "Task deleted com sucesso"}  # Sem ponto de exclamação
    return {"message": "Task not found"}  # Caso não encontre a tarefa
