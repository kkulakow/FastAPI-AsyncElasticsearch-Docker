"""
Connect Elasticsearch. 
&
Search document.
"""
from elasticsearch import AsyncElasticsearch
from sqlalchemy import desc
from sqlalchemy.orm import sessionmaker

from ..db.models.posts import Posts
from ..db.session import engine


class ES_connect:
    def __init__(self) -> None:
        self.es_client = None
        self.connect()

    def connect(self):
        """Connect Elastic.."""
        es = AsyncElasticsearch("http://elasticsearch:9200")
        self.es_client = es
    
    async def search_document(self, index="posts", query="Hello world!"):
        """
        Search document from index by text and sort by created date..
        """
        try:
            response = await self.es_client.search(index="posts", 
                body={"from": 0, "size": 20, "query": 
                        {"match": {"text": query}}, 
                            "sort": "created_date"})
            
            res = []
            result = [res.append(hit["_source"]) for hit in response["hits"]["hits"]]
            return res

        except Exception as e:
            print(e)
    
    async def populate_es(self):
        """
        Filling Elasticsearch with data from the database on the server.
        """
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()
        posts = session.query(Posts).order_by(desc(Posts.created_date)).all()
        for i in posts:
            e1 = {
            "id": i.id,
            "text": i.text,
            "created_date": i.created_date,
            "rubrics": i.rubrics
            }

            await self.es_client.index(index='posts', id=i.id, document=e1)
