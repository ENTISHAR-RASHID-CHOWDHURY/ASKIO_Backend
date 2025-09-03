from pydantic import BaseModel, EmailStr
from typing import Optional, List
from uuid import UUID
from datetime import datetime


# -----------------------
# USER SCHEMAS
# -----------------------
class UserCreate(BaseModel):
    email: EmailStr
    name: Optional[str]
    password: str


class UserOut(BaseModel):
    id: UUID
    email: EmailStr
    name: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True


# -----------------------
# CHAT SESSION SCHEMAS
# -----------------------
class ChatSessionCreate(BaseModel):
    title: Optional[str]


class ChatSessionOut(BaseModel):
    id: UUID
    user_id: UUID
    title: Optional[str]
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True


# -----------------------
# MESSAGE SCHEMAS
# -----------------------
class MessageCreate(BaseModel):
    role: str
    content: str


class MessageOut(BaseModel):
    id: UUID
    chat_id: UUID
    role: str
    content: str
    created_at: datetime

    class Config:
        orm_mode = True


# -----------------------
# COLLECTION SCHEMAS
# -----------------------
class CollectionCreate(BaseModel):
    name: str
    visibility: Optional[str] = "private"


class CollectionOut(BaseModel):
    id: UUID
    owner_id: UUID
    name: str
    visibility: str
    created_at: datetime

    class Config:
        orm_mode = True


# -----------------------
# DOCUMENT SCHEMAS
# -----------------------
class DocumentCreate(BaseModel):
    filename: str
    file_url: Optional[str]
    file_type: Optional[str]


class DocumentOut(BaseModel):
    id: UUID
    collection_id: UUID
    filename: str
    file_url: Optional[str]
    file_type: Optional[str]
    uploaded_at: datetime

    class Config:
        orm_mode = True


# -----------------------
# DOCUMENT EMBEDDING SCHEMAS
# -----------------------
class DocumentEmbeddingCreate(BaseModel):
    embedding: list[float]  # pgvector stored as list of floats
    chunk_index: Optional[int]
    text_chunk: str


class DocumentEmbeddingOut(BaseModel):
    id: UUID
    document_id: UUID
    embedding: list[float]
    chunk_index: Optional[int]
    text_chunk: str

    class Config:
        orm_mode = True


# -----------------------
# SHARED CHAT SCHEMAS
# -----------------------
class SharedChatCreate(BaseModel):
    chat_session_id: UUID
    shared_with_user_id: UUID
    can_edit: Optional[bool] = False


class SharedChatOut(BaseModel):
    id: UUID
    chat_session_id: UUID
    shared_with_user_id: UUID
    can_edit: bool
    shared_at: datetime

    class Config:
        orm_mode = True
