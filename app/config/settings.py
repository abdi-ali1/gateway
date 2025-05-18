import os


class Settings:
    def __init__(self) -> None:
        self.executor_base_url: str = os.getenv("EXECUTOR_BASE_URL", "http://localhost:9001")


settings = Settings()