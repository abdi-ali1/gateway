from fastapi import APIRouter, status
from app.models.execution_request import ExecutionRequest
from app.services.execution_service import ExecutionService


class ExecutionController:
    def __init__(self) -> None:
        self.router = APIRouter()
        self.router.add_api_route(
            path="/run",
            endpoint=self.run,
            methods=["POST"],
            status_code=status.HTTP_202_ACCEPTED
        )

    def run(self, request: ExecutionRequest) -> dict:
        return ExecutionService().run_test(request)