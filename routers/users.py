from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from schemas.users import users
from config.database import session_local
from sqlalchemy.exc import SQLAlchemyError
from services.users import UsersServices

users_router = APIRouter()

@users_router.post('/users',tags=['users'])

def add_users(users:users):
    db = session_local()
    try:
        UsersServices(db).add(users)
        return JSONResponse(content={"message": "User added successfully"}, status_code=201)

    except SQLAlchemyError as e:
        return JSONResponse(content={'error':str(e)},status_code=500)
    
    finally:
        db.close()
        

@users_router.get('/users',tags=['users'],response_model=users)

def get_top_users():
    db = session_local()
    try:
        top = UsersServices(db).get_top()
        return JSONResponse(content=jsonable_encoder(top),status_code=200)
    except SQLAlchemyError as e:
        return JSONResponse(content={'error':str(e)},status_code=500)
    
    finally:
        db.close()

@users_router.get('/users/statistics',tags=['users'],response_model=users)

def get_users_statistics():
    db = session_local()
    try:
        result = UsersServices(db).get_users_by_country()
        return JSONResponse(content=jsonable_encoder(result),status_code=200)
    except SQLAlchemyError as e:
        return JSONResponse(content={'error':str(e)},status_code=500)
    
    finally:
        db.close()