from fastapi import FastAPI, HTTPException
from app.models import Task
from app.database import tasks
from app.services import get_task, add_task, update_task, delete_task

app = FastAPI()


# Rota inicial
@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de Tarefas!"}


# Listar todas as tarefas
@app.get("/tasks")
def list_tasks():
    return tasks


# Criar uma nova tarefa
@app.post("/tasks")
def create_task(task: Task):
    return add_task(task)


# Ler uma tarefa específica pelo ID
@app.get("/tasks/{task_id}")
def read_task(task_id: int):
    task = get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


# Atualizar uma tarefa existente
@app.put("/tasks/{task_id}")
def update_task_route(task_id: int, task: Task):
    updated_task = update_task(task_id, task)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task


# Deletar uma tarefa pelo ID
@app.delete("/tasks/{task_id}")
def remove_task_route(task_id: int):
    if not delete_task(task_id):
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted com sucesso!"}  