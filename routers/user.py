# Post
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from utils.jwt_manager import create_token
from schemas.User_schema import User

login_router = APIRouter()


@login_router.post("/login",tags=["Auth"],status_code=201)
async def login(user:User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token_bytes:str = create_token(user.model_dump())
        return JSONResponse(content=token_bytes)
    else:
        raise JSONResponse(status_code=401,content={"message":"Invalidad data, try again"})