from tabulate import tabulate

class Library:
    def __init__(self):
        self.books = [
            {'id': '1', 'title': '1984', 'author': 'George Orwell', 'year': '1949'},
            {'id': '2', 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': '1960'},
            {'id': '3', 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year': '1925'},
            {'id': '4', 'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'year': '1813'},
            {'id': '5', 'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'year': '1951'}
        ]
        self.users = {}

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!")

    def update_book(self, book_id, updated_info):
        for book in self.books:
            if book['id'] == book_id:
                book.update(updated_info)
                print("Book updated successfully!")
                return
        print("Book not found!")

    def remove_book(self, book_id):
        for i, book in enumerate(self.books):
            if book['id'] == book_id:
                del self.books[i]
                print("Book removed successfully!")
                return
        print("Book not found!")

    def search_book(self, book_id):
        for book in self.books:
            if book['id'] == book_id:
                return book
        print("Book not found!")
        return None

    def view_all_books(self):
        if not self.books:
            print("No books available.")
            return
        headers = ["ID", "Title", "Author", "Year"]
        table = [[book['id'], book['title'], book['author'], book['year']] for book in self.books]
        print(tabulate(table, headers=headers, tablefmt='grid'))

    def register_user(self, username, password):
        if username in self.users:
            print("Already exist")
        else:
            self.users[username] = password
            print("Successfully registered!")

    def login_user(self, username, password):
        if self.users.get(username) == password:
            print("Successfully logged in!")
            return True
        else:
            print("Invalid username or password!")
            return False

def main():
    library = Library()
    logged_in_user = None

    while True:
        if logged_in_user is None:
            print("\nUser Management")
            print("1. Register")
            print("2. Login")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                username = input("Enter username: ")
                password = input("Enter password: ")
                library.register_user(username, password)

            elif choice == '2':
                username = input("Enter username: ")
                password = input("Enter password: ")
                if library.login_user(username, password):
                    logged_in_user = username
                else:
                    continue

            elif choice == '3':
                print("Exiting the system. Goodbye!")
                return

            else:
                print("Invalid choice! Please try again.")
                continue
        else:
            print("\nLibrary Management System")
            print("1. Add Book")
            print("2. Update Book")
            print("3. Remove Book")
            print("4. Search Book")
            print("5. View All Books")
            print("6. Logout")

            choice = input("Enter your choice: ")

            if choice == '1':
                book_id = input("Enter book ID: ")
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                year = input("Enter publication year: ")
                library.add_book({'id': book_id, 'title': title, 'author': author, 'year': year})

            elif choice == '2':
                book_id = input("Enter book ID to update: ")
                updated_info = {}
                title = input("Enter new title (leave blank to skip): ")
                if title:
                    updated_info['title'] = title
                author = input("Enter new author (leave blank to skip): ")
                if author:
                    updated_info['author'] = author
                year = input("Enter new publication year (leave blank to skip): ")
                if year:
                    updated_info['year'] = year
                library.update_book(book_id, updated_info)

            elif choice == '3':
                book_id = input("Enter book ID to remove: ")
                library.remove_book(book_id)

            elif choice == '4':
                book_id = input("Enter book ID to search: ")
                book = library.search_book(book_id)
                if book:
                    print(book)

            elif choice == '5':
                library.view_all_books()

            elif choice == '6':
                logged_in_user = None
                print("Logged out successfully!")

            else:
                print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
