from sqlalchemy import Column, String, Boolean, ForeignKey, Text, TIMESTAMP, Integer
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from pgvector.sqlalchemy import Vector
from app.database import Base


# -----------------------
# USERS
# -----------------------
class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default="gen_random_uuid()")
    email = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=True)
    password_hash = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

    chats = relationship("ChatSession", back_populates="user", cascade="all, delete-orphan")
    collections = relationship("Collection", back_populates="owner", cascade="all, delete-orphan")


# -----------------------
# CHAT SESSIONS
# -----------------------
class ChatSession(Base):
    __tablename__ = "chat_sessions"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default="gen_random_uuid()")
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"))
    title = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP, server_default=func.now())

    user = relationship("User", back_populates="chats")
    messages = relationship("Message", back_populates="chat", cascade="all, delete-orphan")


# -----------------------
# MESSAGES
# -----------------------
class Message(Base):
    __tablename__ = "messages"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default="gen_random_uuid()")
    chat_id = Column(UUID(as_uuid=True), ForeignKey("chat_sessions.id", ondelete="CASCADE"))
    role = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    citation = Column(JSONB, nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now())

    chat = relationship("ChatSession", back_populates="messages")


# -----------------------
# COLLECTIONS
# -----------------------
class Collection(Base):
    __tablename__ = "collections"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default="gen_random_uuid()")
    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"))
    name = Column(String, nullable=False)
    visibility = Column(String, default="private")
    created_at = Column(TIMESTAMP, server_default=func.now())

    owner = relationship("User", back_populates="collections")
    documents = relationship("Document", back_populates="collection", cascade="all, delete-orphan")


# -----------------------
# DOCUMENTS
# -----------------------
class Document(Base):
    __tablename__ = "documents"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default="gen_random_uuid()")
    collection_id = Column(UUID(as_uuid=True), ForeignKey("collections.id", ondelete="CASCADE"))
    filename = Column(String, nullable=False)
    file_url = Column(String, nullable=True)
    file_type = Column(String, nullable=True)
    uploaded_at = Column(TIMESTAMP, server_default=func.now())

    collection = relationship("Collection", back_populates="documents")
    embeddings = relationship("DocumentEmbedding", back_populates="document", cascade="all, delete-orphan")


# -----------------------
# DOCUMENT EMBEDDINGS
# -----------------------
class DocumentEmbedding(Base):
    __tablename__ = "document_embeddings"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default="gen_random_uuid()")
    document_id = Column(UUID(as_uuid=True), ForeignKey("documents.id", ondelete="CASCADE"))
    embedding = Column(Vector(1536))
    chunk_index = Column(Integer, nullable=True)
    text_chunk = Column(Text, nullable=False)

    document = relationship("Document", back_populates="embeddings")


# -----------------------
# SHARED CHATS
# -----------------------
class SharedChat(Base):
    __tablename__ = "shared_chats"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default="gen_random_uuid()")
    chat_session_id = Column(UUID(as_uuid=True), ForeignKey("chat_sessions.id", ondelete="CASCADE"))
    shared_with_user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"))
    can_edit = Column(Boolean, default=False)
    shared_at = Column(TIMESTAMP, server_default=func.now())
