from pydantic import BaseModel, Field
from typing import List, Optional

class Book(BaseModel):
    title: str
    author: str
    is_borrowed: bool = False

class BookOut(Book):
    id: int
