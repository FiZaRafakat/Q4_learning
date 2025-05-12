from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, constr, validator
from typing import Optional
from datetime import datetime, date

class UserCreate(BaseModel):
    user_name: constr(min_length=3, max_length=20)
    email: EmailStr

    @validator('email')
    def validate_email(cls, v):
        if not v.endswith('.com'):
            raise ValueError('Email must end with .com')
        return v

class UserRead(BaseModel):
    user_id: int
    user_name: str
    email: EmailStr

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: date
    user_id: int
    status: str

    @validator('due_date')
    def validate_due_date(cls, v):
        if v < date.today():
            raise ValueError("Due date must be today or in the future.")
        return v

class TaskRead(TaskCreate):
    id: int
    created_at: datetime

class StatusUpdateModel(BaseModel):
    status: str

USERS: dict[int, UserRead] = {}
TASKS: dict[int, TaskRead] = {}
ALLOWED_STATUSES = ['pending', 'in_progress', 'completed']

app = FastAPI()

@app.get('/')
def read_root():
    return {"Hey Welcome to Task Tracker API": "You can create users and tasks and manage them using the API"}

@app.post('/users/', response_model=UserRead)
def create_user(user: UserCreate):
    user_id = len(USERS) + 1
    user_read = UserRead(user_id=user_id, **user.dict())
    USERS[user_id] = user_read
    return user_read

@app.get('/users/{user_id}', response_model=UserRead)
def get_user(user_id: int):
    user = USERS.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not Found")
    return user

@app.post('/tasks/', response_model=TaskRead)
def create_task(task: TaskCreate):
    task_id = len(TASKS) + 1
    new_task = TaskRead(
        id=task_id,
        created_at=datetime.now(),
        **task.dict()
    )
    TASKS[task_id] = new_task
    return new_task

@app.get('/tasks/{task_id}', response_model=TaskRead)
def get_task(task_id: int):
    task = TASKS.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not Found")
    return task

@app.put('/tasks/{task_id}', response_model=TaskRead)
def update_task(task_id: int, update: StatusUpdateModel):
    task = TASKS.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not Found")
    if update.status not in ALLOWED_STATUSES:
        raise HTTPException(status_code=400, detail="Invalid Status")
    task.status = update.status
    return task

@app.get('/users/{user_id}/tasks', response_model=list[TaskRead])
def get_user_tasks(user_id: int):
    user = USERS.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not Found")
    user_tasks = [task for task in TASKS.values() if task.user_id == user_id]
    return user_tasks