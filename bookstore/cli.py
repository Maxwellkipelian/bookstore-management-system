import argparse
from .database import init_db
from .services import add_book, list_books

def main():
    parser = argparse.ArgumentParser(description="Bookstore Management CLI")
    parser.add_argument("command", type=str, choices=["initdb", "add", "list"])
    parser.add_argument("--title", type=str, help="Title of the book")
    parser.add_argument("--author", type=str, help="Author of the book")
    parser.add_argument("--genre", type=str, help="Genre of the book")

    args = parser.parse_args()

    if args.command == "initdb":
        init_db()
        print("Database initialized.")
    elif args.command == "add":
        if args.title and args.author and args.genre:
            add_book(args.title, args.author, args.genre)
        else:
            print("Please provide title, author, and genre for the book.")
    elif args.command == "list":
        books = list_books()
        for book in books:
            print(f"{book.title} by {book.author.name} [{book.genre.name}]")

if __name__ == "__main__":
    main()
