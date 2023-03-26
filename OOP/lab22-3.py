#  Napisz klasę reprezentującą obiekty typu książka, w tym celu:
# • stwórz klasę Book z odpowiednimi właściwościami i metodami,
# • stwórz kilka przykładowych egzemplarzy tej klasy,
# • zademonstruj działanie wybranych metod na przykładowych egzemplarzach.

class Book:

    def __init__(self, title, author, publisher, year):
        self.__title = title
        self.__author = author
        self.__publisher = publisher
        self.__year = year

    def show_short_info(self):
        print("Tytuł: ", self.__title, "autor: ", self.__author )

    def show_full_info(self):
        print("Tytuł: ", self.__title, "autor: ", self.__author, "wydawca: ", self.__publisher ,"rok wyd.: ", self.__year)

books = []
books.append(Book("Dzieci z Bulberbyn","Linda","Egmont",2014))
books.append(Book("Python","John Smith","Znak",2021))
books.append(Book("Elementarz w d","Witold Sapkowski","Helion",2019))

for b in books:
    b.show_full_info()