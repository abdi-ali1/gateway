# Gateway Service for Test Automation Platform

This repository contains the **Gateway Service** for a modular test automation platform using **FastAPI**. It serves as the central API endpoint that accepts test definitions from the frontend and forwards them to the executor microservice.

## ⚙️ Features

- Built with FastAPI and Pydantic
- Receives test instructions in JSON format
- Forwards requests to the executor service via HTTP
- Clean modular structure with separation of concerns (controller, service, client)
- CORS-enabled for local frontend development (default: `http://localhost:5173`)

## 📁 Project Structure

```bash
gateway/
├── app/
│   ├── clients/               # Communicates with the executor service
│   │   └── executor_client.py
│   ├── config/                # Environment and settings
│   │   └── settings.py
│   ├── controllers/           # API routes and logic handlers
│   │   ├── execution_controller.py
│   │   └── routes.py
│   ├── models/                # Request/response models
│   │   └── execution_request.py
│   ├── services/              # Handles internal logic and orchestration
│   │   └── execution_service.py
│   └── main.py                # Application entry point
├── .env                       # Environment variables
├── Dockerfile
├── .dockerignore
├── requirements.txt           # Dependencies

```

## ✨ Example Request
Endpoint: POST /v1/execute/run

```json
{
  "json_config": {
    "name": "login_test",
    "steps": [
      { "keyword": "Open Browser", "args": ["https://example.com", "chrome"] },
      { "keyword": "Input Text", "args": ["id=username", "abdi"] },
      { "keyword": "Click Button", "args": ["id=submit"] }
    ],
    "context": {
      "headless": true
    }
  }
}
```


## 🚀 Run Locally
1. Clone and setup

```bash
git clone https://github.com/abdi-ali1/gateway.git
cd gateway
python -m venv venv
source venv/bin/activate   # Or use venv\Scripts\activate on Windows
pip install -r requirements.txt

```
2. Start the API

```bash
uvicorn app.main:app --reload
```

## 🚚 Forwarding Logic

* The request is received in ExecutionController
* Handled by ExecutionService, which uses ExecutionClient
* Forwarded to the executor microservice (default URL: http://localhost:9001)


## 📄 Environment Variables
Create a .env file:
```env
EXECUTOR_BASE_URL=http://localhost:9001
```

## 👽 Tech Stack
* Python 3.10+
* FastAPI
* httpx
* Pydantic

## 📅 Roadmap / To-do
* Add request validation and logging
* Add authentication and rate limiting
* Add OpenAPI docs customization

## 👤 Author
Abdi Ali
GitHub: @abdi-ali1