from pydantic import BaseModel
from fastapi import FastAPI,Body
from typing import Annotated,Any

app=FastAPI()

class User(BaseModel):
    name:str
    id:int


@app.post("/item/",response_model=User)
async def registerUser(id:Annotated[int,Body()],user:Annotated[str,Body()],password:Annotated[str,Body()])->Any:
    return {'id':id,'name':user,'password':password,'abc':'abc'}