"""
Route for Elasticsearch.
"""
import logging
from types import NoneType
from typing import Optional
from fastapi import APIRouter, status
from starlette.responses import JSONResponse
from starlette.status import HTTP_404_NOT_FOUND

from ..elastic.es_connector import ES_connect


elastic_route = APIRouter()

log = logging.getLogger("uvicorn")

es = ES_connect() # connect to elastic


@elastic_route.get("/elastic/get/", tags=["Elasticsearch"], 
                        description="Get a document with all DB fields.")
async def get(keywords: Optional[str]):
    response = await es.search_document(query=keywords)
    if type(response) == NoneType or len(response) == 0:
        return JSONResponse(status_code=HTTP_404_NOT_FOUND,
            content="Your keywords did not match any documents! Try changing the keywords")
    return response


@elastic_route.post("/fillingES", tags=["Elasticsearch"], 
                description="Filling the Elastic with data from the database.")
async def filling():
    log.info("Initialize filling Elastic from DB...")
    await es.populate_es()
    log.info("Finish filling Elastic.")
    return status.HTTP_200_OK
