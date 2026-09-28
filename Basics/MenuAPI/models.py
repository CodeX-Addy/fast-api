from pydantic import BaseModel
from typing_extensions import List

class MenuItem(BaseModel):
    id: int
    name: str
    category: str
    description: str
    price: float
    available: bool

## in response
class MenuResponse(BaseModel):
    status: str = "success"
    count: int
    items: List[MenuItem]
