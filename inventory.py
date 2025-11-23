
import json
import os
from .book import Book
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATA_FILE = "data/books.json"

class LibraryInventory:
    def __init__(self):
        self.books = []
        self.load_books()

    def add_book(self, title, author, isbn):
         
        for book in self.books:
            if book.isbn == isbn:
                print("Error: Book with this ISBN already exists!")
                return False
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        self.save_books()
        logger.info(f"Added book: {title}")
        print("Book added successfully!")
        return True

    def search_by_title(self, title):
        results = [book for book in self.books if title.lower() in book.title.lower()]
        return results

    def search_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def display_all(self):
        if not self.books:
            print("No books in the library yet.")
        else:
            
            for book in self.books:
                print(book)
            

    def save_books(self):
        os.makedirs("data", exist_ok=True)
        try:
            data = [book.to_dict() for book in self.books]
            with open(DATA_FILE, "w") as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            logger.error(f"Error saving books: {e}")

    def load_books(self):
        if not os.path.exists(DATA_FILE):
            logger.info("No existing data file found. Starting fresh.")
            return
        try:
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                self.books = []
                for item in data:
                    book = Book(item["title"], item["author"], item["isbn"])
                    book.status = item["status"]
                    self.books.append(book)
            logger.info("Books loaded successfully from file.")
        except Exception as e:
            logger.error(f"Error loading books: {e}")
            print("Could not load previous data. Starting with empty library.")