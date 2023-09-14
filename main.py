from fastapi import FastAPI
from config.database import engine_db,Base
from middlewares.error_handler import ErrorHandler 
from routers.anime import anime_router
import os
import uvicorn



app = FastAPI()
app.title = "Aplicacion con FastAPI"
app.version = "0.0.1"
app.add_middleware(ErrorHandler)
app.include_router(anime_router)
Base.metadata.create_all(bind=engine_db)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))