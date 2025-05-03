# tests/test_api.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_summarize_success():
    response = client.post("/summarize", json={"content": "FastAPI is great!"})
    assert response.status_code == 200
    assert response.json() == {"summary": "Summarized content: FastAPI is great!"}

def test_summarize_empty():
    response = client.post("/summarize", json={"content": ""})
    assert response.status_code == 400
    assert response.json()["detail"] == "Content is required"
