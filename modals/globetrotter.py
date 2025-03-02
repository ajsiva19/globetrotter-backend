
from sqlalchemy import  Column, Integer, String, JSON
from utils.database.db_connection import Base

class Destination(Base):
    __tablename__ = "destinations"
    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, index=True)
    country = Column(String)
    clues = Column(JSON)
    fun_facts = Column(JSON)
    trivia = Column(JSON)
