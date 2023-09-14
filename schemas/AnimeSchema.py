
import datetime
from typing import  Optional,Text
from pydantic import BaseModel,Field

class Anime(BaseModel):
    id:Optional[int] = Field(default=None,ge=1,le=2000)
    anime_name:str
    rate:Optional[float] = Field(le=5.0)
    synopsis:str = Text,Field(min_length=50) 
    reviews:Optional[int]
    editor:str
    episodes:Optional[int]
    genres:str = Field(default="accion aventura",min_length=1)
    aired:bool
    year_release:Optional[int] = Field(default=datetime.date.today().year,le=datetime.date.today().year)
    images:str = Field(default="Url images",min_length=1)
    
    class Config:
        schema_extra = {
            "example":{
                "anime_name":"Tu anime",
                "rate":1.9,
                "synopsis":"Una synopsis",
                "reviews":310,
                "editor":"Toei Animation",
                "episodes":1,
                "genres":"comedia aventura",
                "aired":False,
                "year-release":datetime.date.today().year,
                "images":"www.url-images.jpg"
            }
        }


