##############################################
## Class Definitions
##############################################
class StockItem:
    def __init__(self, title, dateAcquired):
        self.__title = title
        self.__dateAcquired = dateAcquired
        self.__onLoan = False

    @property
    def title(self):
        return self.__title

    @property
    def dateAcquired(self):
        return self.__dateAcquired

    @property
    def onLoan(self):
        return self.__onLoan

    @onLoan.setter
    def onLoan(self, value):
        self.__onLoan = value

    def displayDetails(self):
        print(
            f"Item {self.title} acquired on {self.dateAcquired} and loan:{self.onLoan}"
        )


class CD(StockItem):  # is-a relationship
    def __init__(self, title, dateAcquired, artist, playingTime):
        self.__artist = artist
        self.__playingTime = playingTime
        # Initialize the base class
        super().__init__(title, dateAcquired)

    # 1) Write the public getter methods for the artist and the playing time for a CD

    @property
    def artist(self):
        return self.__artist

    @property
    def playingTime(self):
        return self.__playingTime

    # 2) Write the virtual function displayDetails() for a CD

    def displayDetails(self):
        print(
            f"Item {self.title} by {self.artist} with playing time {self.__playingTime} acquired on {self.dateAcquired} and loan : {self.onLoan}"
        )


class Book(StockItem):  # is-a relationship
    def __init__(self, title, dateAcquired, author, isbn):
        self.__author = author
        self.__isbn = isbn
        # Initialize the base class
        super().__init__(title, dateAcquired)

    @property
    def author(self):
        return self.__author

    @property
    def isbn(self):
        return self.__isbn

    def displayDetails(self):
        print(
            f"Item {self.title} by {self.author} with ISBN:{self.isbn} acquired on {self.dateAcquired} and loan:{self.onLoan}"
        )


class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


class Library:
    def __init__(self, name):
        self.__name = name
        self.__books = []
        self.__cds = []
        self.__staff = []

    @property
    def name(self):
        return self.__name

    def hire(self, p):
        self.__staff.append(p)

    def order_book(self, b):
        self.__books.append(b)

    def order_cd(self, c):
        self.__cds.append(c)

    # 3) Create a public method displayDetails() for a Library that prints out who works there, and prints all the details for each book and CD that it has

    def displayDetails(self):
        print("Staff:")
        for s in self.__staff:
            print(s.name)

        print("Books:")
        for b in self.__books:
            b.displayDetails()

        print("CDs:")
        for cd in self.__cds:
            cd.displayDetails()

    # 4) Create a public method takeOutBook(isbn) that will either return a book object (marked as on loan) if that book is in the library and not on loan
    # or return None if that isbn number is not in the library, or it is already on loan.

    def takeOutBook(self, isbn):
        for b in self.__books:
            if b.isbn == isbn and b.onLoan == False:
                b.onLoan = True
                return b
        return None


##############################################
## Main Program
##############################################
alboni = Person("Laura Alboni")
library = Library("Perse")
library.hire(alboni)

harry_potter = Book("Philosopher's Stone", "30/09/2021", "Rowling", "12345678")
fins_album = CD("Favourite worst nightmare", "30/09/2021", "Arctic Monkeys", "1:32")

library.order_book(harry_potter)
library.order_cd(fins_album)

# library.displayDetails()
# library.takeOutBook("12345678")

# 5) Create one more book instance and one more CD instance of your choice, and ask the library to order them

book_2 = Book("Statistics without Tears", "30/09/2021", "Rowntree", "9874891")
cd_2 = CD("Music of the Night", "230/09/2021", "Webber", "5:42")

library.order_book(book_2)
library.order_cd(cd_2)

# 6) Uncomment these lines to test your other code. DO NOT CHANGE THEM

myBooks = []
for i in ("12345678", "98765432", "12345678"):
    book = library.takeOutBook(i)
    if book == None:
        print(f"Cannot take out ISBN:{i}")
    else:
        print("Have book with ISBN:{i}")
        myBooks.append(book)

for b in myBooks:
    b.displayDetails()
