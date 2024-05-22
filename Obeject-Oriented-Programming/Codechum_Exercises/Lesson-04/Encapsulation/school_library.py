# School Library - Python
# by CodeChum Admin

# Implement the class Book with the following details:

# Class - Book:

# Private Properties:
# title (type: str): Represents the title of the book.
# number_of_pages (type: int): Holds the number of pages in the book.
# is_fictional (type: bool): Indicates whether the book is fictional.

# Getters and setters:
# get_title(self) -> str and set_title(self, title: str) - for retrieving and setting the title property
# get_number_of_pages(self) -> int and set_number_of_pages(self, pages: int) - for retrieving and setting the number_of_pages property
# get_is_fictional(self) -> bool and set_is_fictional(self, is_fictional: bool) - for retrieving and setting the is_fictional property

class Book:
    # Class representing a book in a school library
    
    def get_title(self):
        # Getter method for retrieving the title of the book
        return self._title
        
    def set_title(self, title:str):
        # Setter method for setting the title of the book
        self._title = title

    def get_number_of_pages(self):
        # Getter method for retrieving the number of pages in the book
        return self._number_of_pages
        
    def set_number_of_pages(self, number_of_pages: int):
        # Setter method for setting the number of pages in the book
        self._number_of_pages = number_of_pages

    def get_is_fictional(self):
        # Getter method for retrieving whether the book is fictional or not
        return self._is_fictional
        
    def set_is_fictional(self, is_fictional: bool):
        # Setter method for setting whether the book is fictional or not
        self._is_fictional = is_fictional