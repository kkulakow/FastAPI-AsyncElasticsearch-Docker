"""
Start app
"""
import logging
import asyncio

from fastapi import FastAPI
from .db.session import engine
from .db.base import Base
from .api.elastic_route import elastic_route
from .api.home_route import home_route
from .api.delete_route import delete_route
from .api.fillingdb_route import fillingDB_route
from .elastic.es_connector import ES_connect


log = logging.getLogger("uvicorn")


def include_route(app) -> None:
    app.include_router(elastic_route)
    app.include_router(home_route)
    app.include_router(delete_route)
    app.include_router(fillingDB_route)


def create_tables() -> None:
    Base.metadata.create_all(bind=engine)


def start_app() -> FastAPI:
    app = FastAPI(
        title="ElasticAPI",
        version="0.0.1",
        description="A simple search engine application with FastAPI, AsyncElasticsearch and Docker. Developer: Kulakov Kirill i.e. ggtx."
    )

    include_route(app)
    create_tables()
    return app


log.info("Initializing service")
app  = start_app()
log.info("Service finished initializing")


