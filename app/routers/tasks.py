# Import necessary modules
from fastapi import APIRouter
from sqlalchemy.orm import Session

# Import custom modules
from app import crud, models
from app.api import deps

# Initialize router
router = APIRouter()

# Define routes
@router.get("/tasks/", response_model=list[models.Task])
async def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    """

    Retrieve a list of tasks.

    """
    tasks = await crud.task.get_multi(db, skip=skip, limit=limit)
    return tasks

@router.post("/tasks/", response_model=models.Task)
async def create_task(task: models.TaskCreate, db: Session = Depends(deps.get_db)):

    """

    Create a new task.

    """

    return await crud.task.create(db, obj_in=task)
@router.get("/tasks/{task_id}", response_model=models.Task)
async def read_task(task_id: int, db: Session = Depends(deps.get_db)):
    """

    Retrieve a single task.

    """
    task = await crud.task.get(db, id=task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/tasks/{task_id}", response_model=models.Task)
async def update_task(task_id: int, task_update: models.TaskUpdate, db: Session = Depends(deps.get_db)):
    """

    Update a single task.

    """
    db_task = await crud.task.get(db, id=task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return await crud.task.update(db, db_obj=db_task, obj_in=task_update)

@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int, db: Session = Depends(deps.get_db)):
    """

    Delete a single task.

    """
    task = await crud.task.get(db, id=task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    await crud.task.remove(db, id=task_id)
    return {"detail": "Task deleted"}