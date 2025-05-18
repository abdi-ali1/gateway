from fastapi import FastAPI
from app.controllers.execution_controller import ExecutionController
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # 👈 of ["*"] als je alles wil toelaten
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

controller = ExecutionController()
app.include_router(controller.router, prefix="/v1/execute")