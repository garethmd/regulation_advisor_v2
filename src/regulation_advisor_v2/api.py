import logging
from typing import Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, HttpUrl

from .main import run

app = FastAPI()

PORT = 57019

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[f"http://localhost:{PORT}"],  # Frontend URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QueryRequest(BaseModel):
    question: Optional[str] = None


# curl -d '{"question":"what impact does Californian legislation have on a UK company?"}' -H "Content-Type: application/json" -X POST http://localhost:57019/api/query


@app.post("/api/query")
async def kickoff_crew_endpoint(request: QueryRequest):
    try:
        result = run(request.question)
        return {"success": True, "message": result.model_dump_json(indent=2)}
    except Exception as e:
        logging.error(f"Error answering question: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}
