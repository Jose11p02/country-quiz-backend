from fastapi import Request,HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.status import HTTP_403_FORBIDDEN
from config.config import API_KEY

class Apikey_middleware(BaseHTTPMiddleware):
    async def dispatch(self, request:Request, call_next):

        if request.url.path in ['/docs','/openapi.json']:
            response = await call_next(request)
            return response

        if 'x-api-key' not in request.headers:
            raise HTTPException(status_code=HTTP_403_FORBIDDEN,detail='Falta la API key en los headers.')

        api_key = request.headers.get('x-api-key')

        if api_key != API_KEY:
            raise HTTPException(status_code=HTTP_403_FORBIDDEN,detail='Acceso denegado. API key inválida.')
        
        response = await call_next(request)
        return response