from fastapi import FastAPI
from config.database import base,engine
from routers.users import users_router
from middleware.handler_error import HandlerError

app = FastAPI()

app.title = 'country-quiz'

app.version = '1.1'

base.metadata.create_all(bind=engine)

app.include_router(users_router)

app.add_middleware(HandlerError)