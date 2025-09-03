from sqlalchemy.orm import Session
from app import models, schemas
import uuid
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# -----------------------
# HASH PASSWORD
# -----------------------
def hash_password(password: str):
    return pwd_context.hash(password)


# -----------------------
# USER CRUD
# -----------------------
def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = hash_password(user.password)
    db_user = models.User(
        id=uuid.uuid4(),
        email=user.email,
        name=user.name,
        password_hash=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


# -----------------------
# CHAT SESSION CRUD
# -----------------------
def create_chat(db: Session, user_id: str, chat: schemas.ChatSessionCreate):
    db_chat = models.ChatSession(
        id=uuid.uuid4(),
        user_id=uuid.UUID(user_id),  # convert string to UUID
        title=chat.title,
        is_active=True
    )
    db.add(db_chat)
    db.commit()
    db.refresh(db_chat)
    return db_chat


# -----------------------
# MESSAGE CRUD
# -----------------------
def create_message(db: Session, chat_id: str, message: schemas.MessageCreate):
    db_message = models.Message(
        id=uuid.uuid4(),
        chat_id=uuid.UUID(chat_id),  # convert string to UUID
        role=message.role,
        content=message.content
    )
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message


# -----------------------
# COLLECTION CRUD
# -----------------------
def create_collection(db: Session, owner_id: str, collection: schemas.CollectionCreate):
    db_collection = models.Collection(
        id=uuid.uuid4(),
        owner_id=uuid.UUID(owner_id),
        name=collection.name,
        visibility=collection.visibility
    )
    db.add(db_collection)
    db.commit()
    db.refresh(db_collection)
    return db_collection


# -----------------------
# DOCUMENT CRUD
# -----------------------
def create_document(db: Session, collection_id: str, document: schemas.DocumentCreate):
    db_document = models.Document(
        id=uuid.uuid4(),
        collection_id=uuid.UUID(collection_id),
        filename=document.filename,
        file_url=document.file_url,
        file_type=document.file_type
    )
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    return db_document


# -----------------------
# DOCUMENT EMBEDDING CRUD
# -----------------------
def create_document_embedding(db: Session, document_id: str, embedding: schemas.DocumentEmbeddingCreate):
    db_embedding = models.DocumentEmbedding(
        id=uuid.uuid4(),
        document_id=uuid.UUID(document_id),
        embedding=embedding.embedding,
        chunk_index=embedding.chunk_index,
        text_chunk=embedding.text_chunk
    )
    db.add(db_embedding)
    db.commit()
    db.refresh(db_embedding)
    return db_embedding


# -----------------------
# SHARED CHAT CRUD
# -----------------------
def create_shared_chat(db: Session, shared_chat: schemas.SharedChatCreate):
    db_shared_chat = models.SharedChat(
        id=uuid.uuid4(),
        chat_session_id=uuid.UUID(shared_chat.chat_session_id),
        shared_with_user_id=uuid.UUID(shared_chat.shared_with_user_id),
        can_edit=shared_chat.can_edit
    )
    db.add(db_shared_chat)
    db.commit()
    db.refresh(db_shared_chat)
    return db_shared_chat