from fastapi import APIRouter,Depends,Path

from typing import  List
from middlewares.jwt_bearer import  JTWBearer
from fastapi.responses import JSONResponse
from config.database import Session
from fastapi.encoders import jsonable_encoder
from schemas.AnimeSchema import Anime
from services.anime import AnimeServices
from fastapi.responses import HTMLResponse,FileResponse
anime_router = APIRouter()


@anime_router.get("/",tags=["Inicio"],response_class=HTMLResponse)
def root():
    html_file_address = "./public/html/index.html"
    return FileResponse(html_file_address,status_code=200)

@anime_router.get("/animes",tags=["Json Preview"],response_model=List[Anime],dependencies=[Depends(JTWBearer())])
def preview() -> List[Anime]:
    db = Session()
    get_all_data = AnimeServices(db).get_movies()
    return JSONResponse(content=jsonable_encoder
(get_all_data),status_code=200)


@anime_router.get("/anime/{anime_id}",tags=["Filter Animes"],response_model=Anime)
def anime_by_id(anime_id:int = Path(ge=1,le=2000)) -> Anime:
    db = Session()
    result_id = AnimeServices(db).get_anime_by_id(anime_id)
    if not result_id:
        return JSONResponse(status_code=404,content={'message':"Animes not found"})
    return JSONResponse(status_code=200,content=jsonable_encoder(result_id))

@anime_router.get("/animes/",tags=["Filter Animes"],response_model=List[Anime])
def anime_by_category(genre:str) -> List[Anime]:
    db = Session()
    result_by_query  = AnimeServices(db).get_anime_by_genre(genre)
    if not result_by_query:
        return JSONResponse(content={"message":"anime by category not found"},status_code=404)
    return JSONResponse(status_code=200,content=jsonable_encoder(result_by_query)) 


#* POST
@anime_router.post("/anime",tags=["Create anime"],response_model=dict)
async def create_anime(anime: Anime) -> dict:
    db = Session()
    AnimeServices(db).create_anime(anime)
    return JSONResponse(content={"Message": "Anime has been registered successfully"},status_code=201)



#* PUT
@anime_router.put("/anime/{anime_id}",tags=["Update anime"],response_model=dict)
def update_anime(anime_id:int,anime:Anime) -> dict:
        db = Session()
        update_result = AnimeServices(db).get_anime_by_id(anime_id)

        if not update_result:
            return JSONResponse(content={"message":"Anime not found"},status_code=404)
        AnimeServices(db).update_anime(anime_id,anime)
        return JSONResponse(content={"message":"Anime has been modified successfully"},status_code=200)


#! Delete
@anime_router.delete("/anime/{anime_id}",tags=["Delete anime"],response_model=dict,dependencies=[Depends(JTWBearer())])
def delete_anime(anime_id:int = Path(ge=1,le=2000)) -> dict:
    db = Session()
    delete_result = AnimeServices(db).get_anime_by_id(anime_id)
    if delete_result:
        AnimeServices(db).delete_anime(anime_id)
        db.commit()
        return JSONResponse(content={"Message": "Anime has been deleted succefully"},status_code=200)
    if not delete_result:
        return JSONResponse(content={"message":"Anime not found"},status_code=404)
