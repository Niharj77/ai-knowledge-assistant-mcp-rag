from fastapi import FastAPI
from .api.endpoints import router
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(
    title="AI Knowledge Assistant (MCP-based)",
    description="A smart assistant unifying Slack, GitHub, and Notion data."
)

app.include_router(router)

# You can add a root endpoint for a simple health check
@app.get("/")
def read_root():
    return {"message": "AI Knowledge Assistant is up and running!"}
