
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Book:
    def __init__(self, title, author, isbn):
        self.title = title.strip()
        self.author = author.strip()
        self.isbn = isbn.strip()
        self.status = "available"  # available or issued

    def issue(self):
        if self.status == "available":
            self.status = "issued"
            logger.info(f"Book '{self.title}' issued successfully.")
            return True
        else:
            logger.warning(f"Book '{self.title}' is already issued!")
            return False

    def return_book(self):
        if self.status == "issued":
            self.status = "available"
            logger.info(f"Book '{self.title}' returned successfully.")
            return True
        else:
            logger.warning(f"Book '{self.title}' was not issued.")
            return False

    def is_available(self):
        return self.status == "available"

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "status": self.status
        }

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {self.status.upper()}"