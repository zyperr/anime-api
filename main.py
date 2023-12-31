from fastapi import FastAPI
from config.database import engine_db,Base
from middlewares.error_handler import ErrorHandler
from routers.anime import anime_router
from routers.user import login_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.title = "Aplicacion con FastAPI"
app.version = "0.0.1"
app.add_middleware(ErrorHandler)
app.include_router(anime_router)
app.include_router(login_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Base.metadata.create_all(bind=engine_db)




