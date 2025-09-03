from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas, database

router = APIRouter()

@router.post("/users/{user_id}/chats", response_model=schemas.ChatSessionOut)
def create_chat(user_id: str, chat: schemas.ChatSessionCreate, db: Session = Depends(database.get_db)):
    return crud.create_chat(db, user_id, chat)

@router.post("/chats/{chat_id}/messages", response_model=schemas.MessageOut)
def create_message(chat_id: str, message: schemas.MessageCreate, db: Session = Depends(database.get_db)):
    return crud.create_message(db, chat_id, message)

