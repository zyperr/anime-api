from config.database import Base
from sqlalchemy import Column,Integer,String,Float,Text,Boolean


class Anime(Base):
    __tablename__ = "Animes"
    id = Column(Integer,autoincrement=True,primary_key=True)
    anime_name = Column(String)
    rate = Column(Float)
    synopsis = Column(Text)
    reviews  = Column(Integer)
    editor = Column(String)
    episodes = Column(Integer)
    genres = Column(String)
    year_release = Column(Integer)
    aired = Column(Boolean)
    images = Column(String)