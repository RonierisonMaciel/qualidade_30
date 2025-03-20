from fastapi import FastAPI, HTTPException
from app.models import Task
from app.database import tasks
from app.services import get_task, add_task, update_task_in_db, delete_task

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de Tarefas!"}

@app.get("/tasks")
def list_tasks():
    return tasks

@app.post("/tasks")
def create_task(task: Task):
    return add_task(task)

@app.get("/tasks/{task_id}")
def read_task(task_id: int):
    task = get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    task = update_task_in_db(task_id, updated_task)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.delete("/tasks/{task_id}")
def remove_task(task_id: int):
    return delete_task(task_id)
