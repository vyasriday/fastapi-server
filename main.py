from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, ConfigDict

app = FastAPI()
tasks = [
    {'title': 'Learn MCP', 'completed': False, 'id': 1},
    {'title': 'Learn AI', 'completed': False, 'id': 2},]


class TaskCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    title: str = Field(min_length=1, max_length=100)
    completed: bool = False


class TaskResponse(BaseModel):
    id: int
    title: str
    completed: bool


class TaskUpdate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    title: str = Field(min_length=1, max_length=100)
    completed: bool


class TaskPatch(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    title: str | None = Field(default=None, min_length=1, max_digits=100)
    conpleted: bool | None = None


@app.get("/")
def read_root():
    '''
    Root route which returns generic string
    '''
    return {"message": "Hello FastAPI"}


@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks():
    return tasks


@app.get("/tasks/{task_id}", response_model=TaskResponse)
def read_task(task_id: int):
    print(task_id)
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.post("/tasks", response_model=TaskResponse, status_code=201)
def create_task(task: TaskCreate):
    task_data = task.model_dump()
    task_data["id"] = len(tasks) + 1
    print(task_data)
    tasks.append(task_data)
    print(tasks)
    return task_data


@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_update: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:
            task.update(task_update.model_dump())
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.patch("/tasks/{task_id}", response_model=TaskResponse)
def patch_task(task_id: int, task_patch: TaskPatch):
    # With exclude_unset=True, the dictionary contains only fields supplied in the request: {"completed": True}.
    changes = task_patch.model_dump(exclude_unset=True)

    if any(value is None for value in changes.values()):
        raise HTTPException(
            status_code=422,
            detail="Title and completed cannot be null",
        )

    for task in tasks:
        if task["id"] == task_id:
            task.update(changes)
            return task

    raise HTTPException(status_code=404, detail="Task not found")
