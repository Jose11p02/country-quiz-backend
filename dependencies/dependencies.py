from fastapi import Depends, HTTPException,Security
from starlette.status import HTTP_403_FORBIDDEN
from config.config import API_KEY
from fastapi.security.api_key import APIKeyHeader

api_key_header = APIKeyHeader(name='x-api-key')

def validate_api_key(api_key: str = Security(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="API key inválida."
        )