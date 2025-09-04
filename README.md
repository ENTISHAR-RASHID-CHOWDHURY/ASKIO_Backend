# ASKIO Backend

Backend for **ASKIO** built with **FastAPI** and **PostgreSQL**. Supports users, chat sessions, messages, document collections, and embeddings.

---

## Features

- User signup with hashed passwords (bcrypt)  
- Create/manage chat sessions  
- Send/retrieve messages  
- Collections and document management  
- Document embeddings using `pgvector`  
- Database seeding and cleanup scripts  

---

## Tech Stack

- Python 3.11  
- FastAPI  
- SQLAlchemy  
- PostgreSQL  
- pgvector  
- Passlib (bcrypt)  

---

## Setup

```bash
git clone https://github.com/ENTISHAR-RASHID-CHOWDHURY/ASKIO_Backend.git
cd ASKIO-Backend
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
pip install -r requirements.txt
````

Create a `.env` file:

```
DATABASE_URL=postgresql://username:password@localhost:5432/dbname
```

---

## Database Scripts

* Seed database:

```bash
python -m app.seed_db
```

* Cleanup database:

```bash
python -m app.cleanup_db
```

> ⚠️ Only run on dev/test database.

---

## API Endpoints

### Auth

**POST /auth/signup** – Create a new user

```json
{
  "email": "user@example.com",
  "name": "Your Name",
  "password": "yourpassword"
}
```

---

### Chats

**POST /chats/users/{user\_id}/chats** – Create chat session for a user

**POST /chats/chats/{chat\_id}/messages** – Add message to a chat

> `user_id` and `chat_id` must be UUIDs from the database.

---

## Running the Server

```bash
uvicorn app.main:app --reload --log-level debug
```

Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Contributing

1. Fork the repo
2. Create a branch
3. Commit & push changes
4. Open a pull request

---

## License

This project is **open-source**. Feel free to use it for learning.
