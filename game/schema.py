from typing import List
from pydantic import BaseModel, Field, PositiveInt
from typing import Annotated
from annotated_types import Len

class Card(BaseModel):
    color: int
    shade: int
    shape: int
    number: int


class Sets(BaseModel):
    sets: List[str]


class GameConfig(BaseModel):
    cards: Annotated[List[Card], Len(min_length=3, max_length=81)]
    set_size: PositiveInt = Field(ge=3, le=4)
