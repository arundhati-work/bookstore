# Basic Bookstore Inventory System

## Overview:
Create a basic bookstore application where users can view a list of books and see details about each book. Users can also add new books to the inventory. This scenario focuses on CRUD (Create, Read, Update, Delete) operations for book management and a simple user interface.

## Features:

1. **List of Books:** Display all books in the inventory. Show a brief summary (title, author, price) for each book.
2. **Book Details:** When a user clicks on a book, show detailed information (title, author, description, price, and publication date).
3. **Add New Book:** Allow users to add new books to the inventory using a form.
4. **Edit Existing Book:** Provide an option to edit book details.
5. **Delete Book:** Allow users to remove a book from the inventory.

## Models:

**Model = Book:** Represents a book in the inventory.  
**Fields:** title, author, description, price, publication_date

## Views:

1. **Home Page:** Link to view the list of books or create a new book.
2. **List Books:** Display all books with a link to view details.
3. **Book Detail:** Show detailed information about a selected book with links to edit or delete book.
4. **Add Book:** Form to add a new book to the inventory.
5. **Edit Book:** Form to edit the details of an existing book.
6. **Delete Book:** Option to delete a book from the inventory.

## Templates:

1. **home.html:** Links to the list of books.
2. **list_books.html:** Displays all books.
3. **book_detail.html:** Shows detailed information about a book.
4. **book_form.html:** Form to add a book or update an existing book.
