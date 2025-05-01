from typing import Any
from fastapi import FastAPI

app: FastAPI = FastAPI()


@app.get("/notes")
def read_notes() -> list[dict[str, Any]]:
    return [{"id": 1, "content": "Sample note content"}]
