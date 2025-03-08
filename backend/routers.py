from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import Todo
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)   

todo_router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create Task
@todo_router.post("/todos/")
def create_task(task: str, db: Session = Depends(get_db)):
    new_task = Todo(task=task)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

# Get Tasks
@todo_router.get("/todos/")
def get_tasks(db: Session = Depends(get_db)):
    return db.query(Todo).all()

# Mark Task as Complete
@todo_router.put("/todos/{task_id}")
def update_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Todo).filter(Todo.id == task_id).first()
    if task:
        task.completed = True
        db.commit()
        return {"message": "Task completed!"}
    return {"error": "Task not found"}

# Delete Task
@todo_router.delete("/todos/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Todo).filter(Todo.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
        return {"message": "Task deleted!"}
    return {"error": "Task not found"}
