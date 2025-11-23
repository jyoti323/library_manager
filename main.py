import LibraryInventory
import logging

logging.basicConfig(level=logging.INFO)

def main():
    library = LibraryInventory()
    print("Welcome to Library Inventory Manager!")

    while True:
        
        print("1. Add New Book")
        print("2. Issue a Book")
        print("3. Return a Book")
        print("4. Search by Title")
        print("5. Search by ISBN")
        print("6. View All Books")
        print("7. Exit")
        print("="*40)

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            library.add_book(title, author, isbn)

        elif choice == "2":
            isbn = input("Enter ISBN of book to issue: ")
            book = library.search_by_isbn(isbn)
            if book:
                book.issue()
            else:
                print("Book not found!")

        elif choice == "3":
            isbn = input("Enter ISBN of book to return: ")
            book = library.search_by_isbn(isbn)
            if book:
                book.return_book()
            else:
                print("Book not found!")

        elif choice == "4":
            title = input("Enter title to search: ")
            results = library.search_by_title(title)
            if results:
                print(f"\nFound {len(results)} book(s):")
                for b in results:
                    print(b)
            else:
                print("No books found with that title.")

        elif choice == "5":
            isbn = input("Enter ISBN: ")
            book = library.search_by_isbn(isbn)
            if book:
                print(book)
            else:
                print("Book not found!")

        elif choice == "6":
            library.display_all()

        elif choice == "7":
            print("Thank you for using Library Manager. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()