from .models import Book, Author, Genre
from .database import SessionLocal

def add_book(title, author_name, genre_name):
    session = SessionLocal()
    author = session.query(Author).filter(Author.name == author_name).first()
    if not author:
        author = Author(name=author_name)
        session.add(author)

    genre = session.query(Genre).filter(Genre.name == genre_name).first()
    if not genre:
        genre = Genre(name=genre_name)
        session.add(genre)

    book = Book(title=title, author=author, genre=genre)
    session.add(book)
    session.commit()
    session.close()

def list_books():
    session = SessionLocal()
    books = session.query(Book).all()
    session.close()
    return books
