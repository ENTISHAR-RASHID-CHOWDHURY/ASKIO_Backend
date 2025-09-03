from fastapi import FastAPI
from app.database import Base, engine
from app.Routers import auth, chats, documents

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="ASKIO Backend")

# Include Routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(chats.router, prefix="/chats", tags=["chats"])
app.include_router(documents.router, prefix="/documents", tags=["documents"])

