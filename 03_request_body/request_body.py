from fastapi import FastAPI,Body #type:ignore
from pydantic import BaseModel,Field #type:ignore

app=FastAPI()
class User(BaseModel):
    id:int
    name:str = Field(...,len=3)
    cnic:str = Field(...)
    address: str|None =  None

@app.post('/insert')
def addUser(user:User):
    return (user)

@app.put("/user/{user_id}")
async def update_user(user_id: int,user: User, q: str | None = None):
    result = {"user_id": user_id, **user.model_dump()}
    if q:
        result.update({"query": q})
    return result

@app.post('/add_id/')
def addId(id:int =Body(...),name:str=Body(...)):
    return f"{id} {name} added"

 