import httpx
from app.models.execution_request import ExecutionRequest


class ExecutionClient:
    def __init__(self) -> None:
        self.base_url = "http://localhost:9001"

    def send(self, request: ExecutionRequest) -> dict:
        with httpx.Client() as client:
            response = client.post(f"{self.base_url}/run", json=request.model_dump())
            return response.json()