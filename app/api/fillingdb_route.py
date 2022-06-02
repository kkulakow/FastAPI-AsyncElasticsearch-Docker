"""
Route for filling DB from csv-file data.
"""
import logging
from fastapi import APIRouter, status

from ..db.populatedb.populatedb import populate


fillingDB_route = APIRouter()

log = logging.getLogger("uvicorn")


@fillingDB_route.post("/fillingdb", tags=["DB"], 
                description="Filling DB with data from csv-file.")
async def fillingdb():
    log = logging.getLogger("uvicorn")
    log.info("Initialize filling DB...")
    populate()
    log.info("Finish filling DB.")
    return status.HTTP_200_OK
