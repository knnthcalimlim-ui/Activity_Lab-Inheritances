class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        print(f"Book Title: {self.title}") 
        print(f"Author: {self.author}")

class PrintedBook(Book):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages

    def printed_info(self):
        print(f"Printed Book Pages: {self.pages}")

class EBook(PrintedBook):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.file_size = file_size

    def ebook_info(self):
        print(f"EBook File Size: {self.file_size} MB")
