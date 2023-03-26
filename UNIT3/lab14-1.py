#  Napisz wyszukiwarkę numerów telefonów:
# • zdefiniuj słownik par imię -> numer telefonu,
# • zapytaj użytkownika o imię,
# • wyświetl użytkownikowi numer telefonu lub informacje o jego braku.

telephone_book = {
    "Agnieszka":790296763,
    "Robert":111222333,
    "Ola":333222111
}

a = str(input("Do kogo numer potrzebujesz? (" + str(tuple(telephone_book.keys())) + ")"))
if a in telephone_book:
    print(a, "->", telephone_book[a])
else:
    print("Nie znaleziono numeru dla ",a, "w książce.")