# Lumiere

Minimal FastAPI backend with a GPT-like chat completion endpoint.

## Run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Endpoints

- `GET /health`
- `POST /v1/chat/completions`

Example request:

```json
{
  "model": "lumiere-gpt",
  "messages": [
    { "role": "system", "content": "You are helpful." },
    { "role": "user", "content": "Hello!" }
  ]
}
```