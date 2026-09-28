from fastapi import FastAPI, Query, HTTPException
from data import menu_items
from models import MenuItem, MenuResponse
from typing import List

app = FastAPI(
    title="Menu API",
    description="Read only menu listing API"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to your menu listing API!"
    }

@app.get("/menu", response_model=MenuResponse)
def menu(category: str | None = Query(None, description="Filter by tandoor, main course, desserts, breads")):
    if category:
        filtered = [item for item in menu_items if item["category"].lower() == category.lower()]
        if not filtered:
            raise HTTPException(status_code=404, detail=f"The following category is not found: {category}")
        return MenuResponse(count=len(filtered), items=filtered)
    return MenuResponse(count=len(menu_items), items=menu_items)


@app.get("/menu/{item_id}")
def get_item(item_id: int):
    for item in menu_items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail=f"Item with this {item_id} is not found..")
