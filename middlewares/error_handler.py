from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from fastapi import FastAPI,Request,Response
from fastapi.responses import JSONResponse
from typing import Union


class ErrorHandler(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI) -> None:
        super().__init__(app)
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Union[Response,JSONResponse]:
        try:
            return await call_next(request)
        except Exception as err:
            return JSONResponse(status_code=500,content={"error":str(err)})
