from models.anime import Anime as Anime_Model
from schemas.AnimeSchema import Anime


class AnimeServices():
    def __init__(self,db) -> None:
        self.db = db

    def get_animes(self):
        result = self.db.query(Anime_Model).all()
        return result
    
    def get_anime_by_id(self,anime_id):
        result = self.db.query(Anime_Model).filter(Anime_Model.id == anime_id).first()
        return result
    
    def get_anime_by_query(self,genre,year):
        if genre != "":
            result = self.db.query(Anime_Model).filter(Anime_Model.genres.contains(genre)).all()
        elif year is not None:
            result = self.db.query(Anime_Model).filter(Anime_Model.year_release == year).all()

        if genre != "" and year is not None:
            result = self.db.query(Anime_Model).filter(Anime_Model.genres.contains(genre),Anime_Model.year_release == year).all()
        
        return result
    
    def create_anime(self,anime:Anime):
        new_anime = Anime_Model(**anime.model_dump())
        self.db.add(new_anime)
        self.db.commit()
    
    def update_anime(self,anime_id:int,data:Anime):
        anime = self.get_anime_by_id(anime_id)

        anime.anime_name = data.anime_name 
        anime.rate  = data.rate 
        anime.synopsis = data.synopsis
        anime.reviews = data.reviews
        anime.editor = data.editor
        anime.episodes = data.episodes
        anime.genres = data.genres
        anime.aired = data.aired
        anime.year_release = data.year_release
        anime.images = data.images
        self.db.commit()
        
    def delete_anime(self,anime_id):
        result = self.db.query(Anime_Model).filter(Anime_Model.id == anime_id).first()
        self.db.delete(result)
        self.db.commit()