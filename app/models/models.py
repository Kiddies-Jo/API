# app/models.py
from datetime import datetime
from pydantic import BaseModel


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    hashed_password: str
    date_of_birth: datetime
    cities: str
    address_location: str


class EmailAndPassword(BaseModel):
    email: str
    password: str


class ItemUserSelectorCreate(BaseModel):
    color: str
    number_of_items: int


class ItemCreate(BaseModel):
    name: str
    image_or_video: str
    description: str
    price: float
