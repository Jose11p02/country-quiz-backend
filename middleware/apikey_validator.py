from fastapi import Request,HTTPException,FastAPI,Response
from fastapi.security import APIKeyHeader
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.status import HTTP_403_FORBIDDEN
from config.config import API_KEY

api_key_header = APIKeyHeader(name='x-api-key',auto_error=False)

class Apikey_middleware(BaseHTTPMiddleware):

    def __init__(self, app:FastAPI, dispatch = None):
        super().__init__(app, dispatch)

    async def dispatch(self, request:Request, call_next):

        try:

            if request.url.path in ['/docs','/openapi.json']:
                return await call_next(request)

            api_key = request.headers.get('x-api-key')

            if not api_key:
                return Response(
                    content='{"detail": "API key missing from headers."}',
                    status_code=HTTP_403_FORBIDDEN,
                    media_type='application/json'
                )

            if api_key != API_KEY:
                return Response(
                    content='{"detail": "Access denied. Invalid API key."}',
                    status_code=HTTP_403_FORBIDDEN,
                    media_type='application/json'
                )            
            return await call_next(request)
        except HTTPException as e:
            raise e
        
        except Exception as e:
            raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail=f"Error en la validación de API key: {str(e)}")