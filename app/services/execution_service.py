from app.models.execution_request import ExecutionRequest
from app.clients.executor_client import ExecutionClient


class ExecutionService:
    def __init__(self) -> None:
        self.client = ExecutionClient()

    def run_test(self, request: ExecutionRequest) -> dict:
        return self.client.send(request)
