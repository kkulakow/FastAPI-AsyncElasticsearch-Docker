"""
Welcome route.
"""
import logging
from fastapi import APIRouter, Request, Response
import logging

home_route = APIRouter()

log = logging.getLogger("uvicorn")


@home_route.get("/", tags=["Welcome"])
async def home(request: Request):
    return ("Welcome to FastAPI + Elasticsearch created by GGTX. Go to /docs!")



@home_route.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down... Goodbye!")
