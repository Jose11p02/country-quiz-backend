from fastapi import FastAPI
from config.database import base,engine
from routers.users import users_router
from middleware.handler_error import HandlerError
from middleware.apikey_validator import Apikey_middleware
from fastapi.middleware.cors import CORSMiddleware
from decouple import config

app = FastAPI()

origin = config('ALLOWED_ORIGINS',default='http://localhost:3000').split(',')

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.title = 'country-quiz'

app.version = '1.1'

base.metadata.create_all(bind=engine)

app.include_router(users_router)

app.add_middleware(HandlerError)

app.add_middleware(Apikey_middleware)