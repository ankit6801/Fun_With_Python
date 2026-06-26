class Book:
    def __init__(self,title):
        self.title = title
        self.available = True

    def issue(self):
        if self.available:
            self.available = False
            print(f"{self.title} issued successfully.")
        else:
            print("Book not available.")

    def return_book(self):
        self.available = True
        print(f"{self.title} returned.")
book = Book("Python")
book.issue()
book.return_book()