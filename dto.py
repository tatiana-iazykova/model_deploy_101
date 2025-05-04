import datetime

from pydantic import BaseModel


class Card(BaseModel):
    Title: str
    Description: str
    NmId: int


class ItemCardIn(BaseModel):
    uuid: str
    received_at: datetime.datetime
    card: Card


class ItemCardOut(BaseModel):
    label: int
