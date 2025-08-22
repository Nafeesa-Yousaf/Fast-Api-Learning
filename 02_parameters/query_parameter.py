from fastapi import FastAPI #type:ignore

app=FastAPI()

#optional query parameteers
@app.get("/items")
def items(q:int|None=None):
    if q:
        return {'items': "Items", "q":q}
    return {'items': "Items"}

#Default Parameters

@app.get("/items/default")
def items(q:int =0):
    if q:
        return {'items': "Items", "q":q}
    return {'items': "Items"}


#both optional and default
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str,short: bool, q: str | None = None, ):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
