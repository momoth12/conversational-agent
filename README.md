# Chatbot API

A FastAPI chatbot powered by Mistral AI with MongoDB Atlas for conversation history persistence.

## Tech Stack

- **FastAPI** — REST API framework
- **Mistral AI** — LLM provider (mistral-large-latest)
- **MongoDB Atlas** — Chat history storage
- **Pydantic** — Request/response validation

## Project Structure

```
chatbot/
├── .env                  # API keys + MongoDB URI
├── requirements.txt
├── test.py               # MongoDB connection test
└── app/
    ├── __init__.py
    ├── main.py            # FastAPI app entry point
    ├── models.py          # Pydantic schemas
    ├── routes.py          # /chat endpoint
    └── services.py        # Mistral + MongoDB clients
```

## Setup

### 1. Clone and create environment

```bash
conda create -n chatbot python=3.11
conda activate chatbot
pip install -r requirements.txt
```

### 2. Configure environment variables

Create a `.env` file at the project root:

```
MISTRAL_API_KEY=your_mistral_api_key
MONGO_URI=mongodb+srv://<user>:<password>@<cluster>.mongodb.net/?appName=Cluster0
```

### 3. Test MongoDB connection

```bash
python test.py
```

### 4. Run the server

**PowerShell (Windows):**

```powershell
$env:SSL_CERT_FILE = python -c "import certifi; print(certifi.where())"
uvicorn app.main:app --reload
```

**Bash (Linux/macOS):**

```bash
export SSL_CERT_FILE=$(python -c "import certifi; print(certifi.where())")
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.

## API Usage

### POST /chat

Send a message and get a response. Messages are persisted per `session_id`.

**Request:**

```json
{
  "session_id": "user-123",
  "message": "Hello, who are you?"
}
```

**Response:**

```json
{
  "response": "I'm a simple chatbot here to help. What's up?"
}
```

### Example with curl

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"session_id": "user-123", "message": "Hello!"}'
```

### Swagger UI

Interactive API docs available at `http://localhost:8000/docs`.

## How It Works

1. Client sends a message with a `session_id`
2. Server loads conversation history for that session from MongoDB
3. Full history + new message is sent to Mistral AI
4. User message and assistant reply are saved to MongoDB
5. Response is returned to the client

Using the same `session_id` across requests maintains conversation context.
