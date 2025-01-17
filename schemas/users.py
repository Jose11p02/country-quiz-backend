from pydantic import BaseModel,Field
from typing import Optional

class users(BaseModel):
    id:Optional[int] = None
    nick:str
    country:str
    score:int

    class Config:
        json_schema_extra = {
            'example':{
                'nick':'jones',
                'country':'spain',
                'score':3
            }
        }