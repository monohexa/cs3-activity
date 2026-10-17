class Publication:
    def __init__(self, title: str, author: str):
        self.__title: str = title
        self.__author: str = author
    def get_title(self):
        return f"Title: {self.__title}"
    def get_author(self):
        return f"Author: {self.__author}"
    def set_title(self, title: str):
        self.__title = title
    def set_author(self, author: str):
        self.__author = author
    def display_info(self):
        print(self.get_title())
        print(self.get_author())

class Book(Publication):
    def __init__(self, title: str, author: str, number_pages: int):
        super().__init__(title, author)
        if number_pages >= 1:
            self.__number_of_pages: int = number_pages
        else:
            print("Number of pages must be positive.")
            return
    def get_number_of_pages(self):
        return f"Number of pages: {self.__number_of_pages}"
    def set_number_of_pages(self, number_pages: int):
        if number_pages >= 1:
            self.__number_of_pages = number_pages
        else:
            print("Number of pages must be positive.")
            return

class Magazine(Publication):
    def __init__(self, title: str, author: str, issue_number: int):
        super().__init__(title, author)
        if issue_number >= 1:
            self.__issue_number: int = issue_number
        else:
            print("Issue number must be positive.")
            return
    def get_issue_number(self):
        return f"Issue number: {self.__issue_number}"
    def set_issue_number(self, issue_number: int):
        if issue_number >= 1:
            self.__issue_number = issue_number
        else:
            print("Issue number must be positive.")
            return

# objs
pub1 = Publication(
    "Journal of Experimental Psychology", 
    "Ratchiff, R. & Van Dongen, H."
)
book1 = Book(
    "The Hobbit",
    "J.R.R. Tolkien",
    310
)
mag1 = Magazine(
    "National Geographic",
    "Various Authors",
    202
)

print("Publication Information:")
pub1.display_info()

print("\nBook Information:")
book1.set_number_of_pages(-310)
book1.display_info()
print(book1.get_number_of_pages())

print("\nMagazine Information:")
mag1.display_info()
print(mag1.get_issue_number())