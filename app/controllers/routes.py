from fastapi import APIRouter, status
from gateway.models.request import RunTestRequest
from gateway.clients.test_executor_client import forward_test

router = APIRouter()

class TestController:
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/run", self.run_test, methods=["POST"], status_code=202)

    def run_test(self, request: RunTestRequest):
        return TestExecutorClient().forward(request)
