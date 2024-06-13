# Bookstore CLI Application

### Author: Maxwell Kipelian
### Date: June 10, 2024

---

## Description

The Bookstore CLI Application is a command-line interface tool designed to manage a bookstore's inventory. This application allows users to add, update, delete, and view books, while also managing author and genre information. It is built with best practices in mind, leveraging SQLAlchemy ORM for database interactions and maintaining a clean package structure.

---

## Features

- **Add Books**: Add new books to the inventory.
- **Update Books**: Update existing book details.
- **Delete Books**: Remove books from the inventory.
- **View Books**: List all books in the inventory.
- **Manage Authors**: Automatically handle authors when books are added or updated.
- **Manage Genres**: Automatically handle genres when books are added or updated.

--
## Usage

1. **Add a book:**
    ```sh
    python app/cli.py add --title "Book Title" --author "Author Name" --genre "Genre" --price "Price"
    ```

2. **Update a book:**
    ```sh
    python app/cli.py update --book_id 1 --title "New Book Title" --author "New Author Name" --genre "New Genre" --price "New Price"
    ```

3. **Delete a book:**
    ```sh
    python app/cli.py delete --book_id 1
    ```

4. **View all books:**
    ```sh
    python app/cli.py view
    ```

---

## Technologies Used

- **Python**: The main programming language.
- **Click**: For creating the CLI.
- **SQLAlchemy**: ORM for database interactions.
- **SQLite**: Database management system.
- **Pipenv**: For managing the virtual environment and dependencies.

---

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---
