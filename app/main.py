from __future__ import annotations

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from teenify import teenify as teenify_func

app = FastAPI(
    title="Teenify API",
    description="A simple API to convert plain text into exaggerated teen slang.",
    version="0.1.0"
)

class TeenifyRequest(BaseModel):
    text: str

class TeenifyResponse(BaseModel):
    result: str

@app.post("/api/teenify", response_model=TeenifyResponse)
async def api_teenify(request: TeenifyRequest):
    """Convert input text into exaggerated teen slang."""
    if not request.text:
        raise HTTPException(status_code=400, detail="No input text provided")
    return TeenifyResponse(result=teenify_func(request.text))
