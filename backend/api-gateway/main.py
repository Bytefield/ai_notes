from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import httpx

app: FastAPI = FastAPI()

NOTES_SERVICE_URL = "http://notes-service:8001"
SUMMARIZER_SERVICE_URL = "http://summarizer-service:8002"


@app.api_route("/api/notes", methods=["GET", "POST"])
async def proxy_notes(request: Request) -> JSONResponse:
    try:
        async with httpx.AsyncClient() as client:
            data = await request.json() if request.method != "GET" else None
            backend_response = await client.request(
                method = request.method,
                url = f"{NOTES_SERVICE_URL}/notes",
                json = data,
            )
        return JSONResponse(content=backend_response.content, status_code=backend_response.status_code)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.api_route("/api/summarize", methods=["POST"])
async def proxy_summarize(request: Request) -> JSONResponse:
    try:
        data = await request.json()
        async with httpx.AsyncClient() as client:
            backend_response = await client.post(
                url = f"{SUMMARIZER_SERVICE_URL}/summarize",
                json = data,
            )
        return JSONResponse(content=backend_response.content, status_code=backend_response.status_code)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
