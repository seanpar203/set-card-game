from typing import List
from pydantic import BaseModel


class Card(BaseModel):
    color: str
    shade: str
    shape: str
    number: str


class Cards(BaseModel):
    cards: List[Card]


class Sets(BaseModel):
    sets: List[List[Card]]
