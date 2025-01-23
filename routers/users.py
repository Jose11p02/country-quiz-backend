from fastapi import APIRouter,Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from schemas.users import users
from config.database import session_local
from sqlalchemy.exc import SQLAlchemyError
from services.users import UsersServices
from dependencies.dependencies import validate_api_key

users_router = APIRouter()

@users_router.post('/users',tags=['users'],dependencies=[Depends(validate_api_key)])

def add(users:users):
    db = session_local()
    try:
        UsersServices(db).add(users)
    except SQLAlchemyError as e:
        return JSONResponse(content={'error':str(e)},status_code=500)
    
    finally:
        db.close()
        

@users_router.get('/users',tags=['users'],response_model=users,dependencies=[Depends(validate_api_key)])

def get_top():
    db = session_local()
    try:
        top = UsersServices(db).get_top()
        return JSONResponse(content=jsonable_encoder(top),status_code=200)
    except SQLAlchemyError as e:
        return JSONResponse(content={'error':str(e)},status_code=500)
    
    finally:
        db.close()

@users_router.get('/users/statistics',tags=['users'],response_model=users,dependencies=[Depends(validate_api_key)])

def get_statistics():
    db = session_local()
    try:
        result = UsersServices(db).get_users_by_country()
        return JSONResponse(content=jsonable_encoder(result),status_code=200)
    except SQLAlchemyError as e:
        return JSONResponse(content={'error':str(e)},status_code=500)
    
    finally:
        db.close()