from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..rag.pipeline import get_response_from_rag
# Import other necessary modules for data ingestion

router = APIRouter()

class QueryRequest(BaseModel):
    query: str

@router.post("/query")
def query_assistant(request: QueryRequest):
    try:
        response = get_response_from_rag(request.query)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
