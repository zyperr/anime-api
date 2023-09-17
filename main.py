from fastapi import FastAPI
from config.database import engine_db,Base
from middlewares.error_handler import ErrorHandler 
from routers.anime import anime_router
from routers.user import login_router
from fastapi.responses import HTMLResponse,FileResponse
from fastapi.staticfiles import StaticFiles




app = FastAPI()
app.title = "Aplicacion con FastAPI"
app.version = "0.0.1"
app.add_middleware(ErrorHandler)
app.include_router(anime_router)
app.include_router(login_router)


Base.metadata.create_all(bind=engine_db)




app.mount("/static",StaticFiles(directory="./static"),name="static")

@app.get("/",tags=["Inicio"],response_class=HTMLResponse)
def root():
    html_file_address = "./static/index.html"
    return FileResponse(html_file_address,status_code=200)