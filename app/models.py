## /app/models.py
from pydantic import BaseModel

# Definindo o modelo Task usando Pydantic
class Task(BaseModel):
    id: int
    title: str
    description: str
    completed: bool
