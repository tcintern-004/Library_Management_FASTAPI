from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional

import models
import schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/books", response_model=schemas.BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    new_book = models.Book(
        title=book.title, 
        author=book.author, 
        is_published=book.is_published
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@app.get("/books", response_model=List[schemas.BookResponse])
def get_books(search: Optional[str] = "", db: Session = Depends(get_db)):
    books = db.query(models.Book).filter(models.Book.title.contains(search)).all()
    return books

@app.get("/books/{id}", response_model=schemas.BookResponse)
def get_book(id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == id).first()
    
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with ID {id} not found")
        
    return book

@app.put("/books/{id}", response_model=schemas.BookResponse)
def update_book(id: int, updated_book: schemas.BookCreate, db: Session = Depends(get_db)):
    book_query = db.query(models.Book).filter(models.Book.id == id)
    book = book_query.first()
    
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with ID {id} not found")
        
    book_query.update(updated_book.model_dump(), synchronize_session=False)
    db.commit()
    
    return book_query.first()

@app.delete("/books/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(id: int, db: Session = Depends(get_db)):
    book_query = db.query(models.Book).filter(models.Book.id == id)
    book = book_query.first()
    
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with ID {id} not found")
        
    book_query.delete(synchronize_session=False)
    db.commit()
    
    return None