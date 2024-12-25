from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import get_todos, get_todo, create_todo, delete_todo, update_todo
from schemas import Todo, TodoCreate
from db import get_db

router = APIRouter(prefix="/items", tags=["Todo Items"])


@router.get("", response_model=list[Todo])
def read_todos(db: Session = Depends(get_db)):
    return get_todos(db)


@router.get("/{item_id}", response_model=Todo)
def read_todo(item_id: int, db: Session = Depends(get_db)):
    db_todo = get_todo(db, item_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_todo


@router.post("", response_model=Todo)
def create_todo_item(todo: TodoCreate, db: Session = Depends(get_db)):
    return create_todo(db, todo)


@router.delete("/{item_id}")
def delete_todo_item(item_id: int, db: Session = Depends(get_db)):
    delete_todo(db, item_id)
    return {"message": "item deleted"}


@router.put("/{item_id}", response_model=Todo)
def update_todo_item(item_id: int, todo: TodoCreate, db: Session = Depends(get_db)):
    updated_todo = update_todo(db, item_id, todo)
    if not updated_todo:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_todo
