from fastapi import FastAPI, Request
import httpx

app: FastAPI = FastAPI()


@app.api_route("full_path/path", methods=["GET", "POST", "PUT", "DELETE"])
async def proxy(reqquest: Request, full_path: str) -> dict[str, str]:
    return {"message": "Proxy route"}
