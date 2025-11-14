from fastapi import FastAPI, HTTPException
from .schemas import Book, BookOut
from typing import List

app = FastAPI()


# ----- GLOBAL LIST OF BOOKS -----
books = [
    {
        "id": 0,
        "title": "What is FastAPI",
        "author": "Aneesh Sunganahalli",
        "is_borrowed": False,
    },
    {"id": 1, "title": "Learning Python", "author": "Bob", "is_borrowed": True},
]


@app.get("/")
def root():
    message = {"message": "Welcome to my API :)"}
    return message


@app.get("/books", response_model=List[BookOut])
def get_all_books():
    return books


@app.get("/books/{book_id}", response_model=BookOut)
def get_book_by_id(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.get("/borrowed", response_model=List[BookOut])
def get_borrowed_books():
    borrowed_books = []
    for book in books:
        if book["is_borrowed"] == True:
            borrowed_books.append(book)
    return borrowed_books


@app.post("/books/create")
def create_new_book(book: Book):
    new_book = book.model_dump()
    # Generate new ID
    new_id = max([b["id"] for b in books], default=-1) + 1
    new_book["id"] = new_id
    books.append(new_book)
    return {"message": "Book created successfully", "book": new_book}


@app.delete("/books/delete/{book_id}")
def delete_book(book_id: int):
    N = len(books)
    for i in range(N):
        if books[i]["id"] == book_id:
            deleted = books.pop(i)
            return {"message": "Book deleted successfully", "book": deleted}
    raise HTTPException(status_code=404, detail="Book not found")


@app.put("/books/update/{book_id}")
def update_book(book_id: int, book: Book):
    N = len(books)
    for i in range(N):
        if books[i]["id"] == book_id:
            books[i] = book.model_dump()
            books[i]["id"] = book_id
            return {"message": "Book updated successfully", "book": books[i]}
    raise HTTPException(status_code=404, detail="Book not found")