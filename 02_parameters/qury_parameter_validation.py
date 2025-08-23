from fastapi import FastAPI, Query #type:ignore
from typing import Annotated
from pydantic import conlist, constr#type:ignore

app = FastAPI()

# Define constrained list
ItemList = conlist(constr(pattern="^[a-z]+$"), min_length=2, max_length=5)

@app.post("/items/")
def item(q: Annotated[ItemList, Query(alias="item-name")] = ["a", "b"]):
    return {"items": q}
