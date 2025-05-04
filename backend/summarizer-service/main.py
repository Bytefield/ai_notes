from fastapi import FastAPI, HTTPException, Request
import openai
import os

app: FastAPI = FastAPI()
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.post("/summarize")
async def summarize(request: Request) -> dict[str, str]:

    data = await request.json()
    content: str = data.get("content", "")

    if not content:
        raise HTTPException(status_code=400, detail="Content is required")

    return {"summary": f"Summarized content: {content}"}
