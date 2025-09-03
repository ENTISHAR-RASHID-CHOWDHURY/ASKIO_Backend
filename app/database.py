from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# ✅ Use smaller pool size for Supabase Session Pooler
engine = create_engine(
    DATABASE_URL,
    pool_size=5,            # limit connections (important for Supabase free tier)
    max_overflow=0,         # don’t create extra connections
    pool_timeout=30,        # wait max 30s for a connection
    pool_recycle=1800,      # recycle connections every 30 min
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


