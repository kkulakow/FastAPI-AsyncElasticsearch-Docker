from sqlalchemy import Integer, String, DateTime, Table, Column
import datetime

from ..base_class import Base


class Posts(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    rubrics = Column(String)
    