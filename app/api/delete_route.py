"""
Route for delete post from DB and Elasticsearch by id.
"""
from elasticsearch import AsyncElasticsearch
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from starlette.status import HTTP_404_NOT_FOUND

from ..elastic.es_connector import ES_connect
from ..db.session import get_db
from ..db.models.posts import Posts

delete_route = APIRouter()
es = ES_connect()

async def delete_post(id, db):
    """Delete from DB"""
    post = db.query(Posts).filter(Posts.id == id).delete(synchronize_session=False)
    db.commit()
    

@delete_route.delete("/delete/{id}", tags=["Delete from ES & DB"], 
                description="Delete post from Index and Database.")
async def delete(id: int, db: Session = Depends(get_db)):

    client = AsyncElasticsearch("http://elasticsearch:9200")
    try:
        await client.delete(index='posts', id=id)
    except:
        return JSONResponse(HTTP_404_NOT_FOUND, content="Post not found in Elastic")
    try:
        await delete_post(id=id, db=db)
    except:
        return JSONResponse(HTTP_404_NOT_FOUND, content="Post not found in DB")
    return status.HTTP_200_OK
