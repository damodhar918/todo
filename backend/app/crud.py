from sqlalchemy.orm import Session
from app.models.todo import Todo
from app.models.schemas import TodoCreate, TodoUpdate
from typing import List, Optional

def get_todos(db: Session, skip: int = 0, limit: int = 100) -> List[Todo]:
    """Get all todos with pagination"""
    return db.query(Todo).offset(skip).limit(limit).all()

def get_todo(db: Session, todo_id: int) -> Optional[Todo]:
    """Get a specific todo by ID"""
    return db.query(Todo).filter(Todo.id == todo_id).first()

def create_todo(db: Session, todo: TodoCreate) -> Todo:
    """Create a new todo"""
    db_todo = Todo(
        title=todo.title,
        description=todo.description,
        completed=todo.completed
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo(db: Session, todo_id: int, todo_update: TodoUpdate) -> Optional[Todo]:
    """Update an existing todo"""
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not db_todo:
        return None
    
    update_data = todo_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_todo, field, value)
    
    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, todo_id: int) -> bool:
    """Delete a todo"""
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not db_todo:
        return False
    
    db.delete(db_todo)
    db.commit()
    return True