class Book:

    def __init__(self, title, author, isbn, genre):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre

    def details(self):
        print("Hello, the name of your book is "+self.title+" and it's author is "+self.author+"")

    def availability(self):
        user_budget = float(input("Enter your budget: "))

        if user_budget < 20:
            print("You cannot afford book called "+self.title+"")
        else:
            print("Book called "+self.title+" is available to you")
    
    def borrow(self):
        user_days = int(input("Enter how many days you want to borrow this book: "))

        if user_days > 14:
            print("You are not let to borrow book called "+self.title+"")
        else:
            print("You can borrow book called "+self.title+" for the total of 14 days")
    
book_1 = Book("Data Tutashkhia", "Chabua Amirejibi", 10, "Novel")

print(book_1.author)
print(book_1.title)
print(book_1.genre)
book_1.details()
book_1.availability()
book_1.borrow()