from fastapi import FastAPI #type:ignore
from enum import Enum
app=FastAPI()

#pass parameters
@app.get('/items/{item_id}')
async def item(item_id:int):
    return {'message':item_id}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

#Enum for predefine values
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

#path converter

@app.get("/files/{file_path:path}")
def file(file_path:str):
    return {file_path}