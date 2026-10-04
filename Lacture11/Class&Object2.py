class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False  # instance variable to track if the book is checked out

    def check_out (self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return f"{self.title} has been checked out."
        else:
            return f"{self.title} is already checked out."

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return f"{self.title} has been returned."
        else:
            return f"{self.title} was not checked out."

book1 = Book("To Kill a Mockingbird", "Harper Lee", "978-0-06-112008-4")
book2 = Book("1984", "George Orwell", "978-0-452-28423-4")

print(book1.check_out())
print(book2.return_book())
print(book1.check_out())