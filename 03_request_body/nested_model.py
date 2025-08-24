from fastapi import FastAPI, Body
from pydantic import BaseModel, HttpUrl
from typing import Annotated

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    images: list[Image] | None = None


class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]


@app.post("/offers/")
async def create_offer(
    offer: Annotated[
        Offer,
        Body(
            openapi_examples={
                "normal": {
                    "summary": "Normal offer",
                    "description": "A standard offer with two items and images",
                    "value": {
                        "name": "Summer Sale",
                        "description": "Discount on selected items",
                        "price": 99.99,
                        "items": [
                            {
                                "name": "Laptop",
                                "description": "A powerful laptop",
                                "price": 1200,
                                "tax": 120,
                                "tags": ["electronics", "computer"],
                                "images": [
                                    {"url": "http://example.com/laptop.png", "name": "Front view"},
                                    {"url": "http://example.com/laptop-back.png", "name": "Back view"},
                                ],
                            },
                            {
                                "name": "Mouse",
                                "description": "Wireless mouse",
                                "price": 25,
                                "tags": ["electronics", "accessory"],
                                "images": [
                                    {"url": "http://example.com/mouse.png", "name": "Product view"}
                                ],
                            },
                        ],
                    },
                },
                "minimal": {
                    "summary": "Minimal offer",
                    "description": "Only required fields, no optional data",
                    "value": {
                        "name": "Basic Deal",
                        "price": 50,
                        "items": [
                            {
                                "name": "Keyboard",
                                "price": 20
                            }
                        ],
                    },
                },
                "invalid": {
                    "summary": "Invalid data example",
                    "description": "Price is given as string instead of number",
                    "value": {
                        "name": "Broken Offer",
                        "price": "cheap",
                        "items": [
                            {
                                "name": "Monitor",
                                "price": "two hundred"
                            }
                        ],
                    },
                },
            }
        ),
    ]
):
    return offer
