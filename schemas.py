from typing import List

from pydantic import BaseModel, validator, Field
from datetime import date


class Genres(BaseModel):
    name: str


class Author(BaseModel):
    first_name: str = Field(..., max_length=25)
    last_name: str
    age: int = Field(..., gt=15, lt=90, description='years old')

    @validator('age')
    def check_age(self, v):
        if v < 15:
            raise ValueError('Not enough years')
        return v


class Book(BaseModel):
    title: str
    writer: str
    duration: str
    date: date
    summary: str
    genres: List[Genres] = []
    pages: int


class BookOut(Book):
    id: int