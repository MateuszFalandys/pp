# Napisz skrypt wyświetlający na ekranie macierz. Rozmiar macierzy oraz
# znak z jakiej będzie zbudowana powinien określić użytkownik.
print("Program wyświetlający macierz o zadanych parametrach")
size = int(input("Podaj wymiar macierzy:"))
symbol = input("Podaj symbol wypełnienia macierzy:")


for i in range (1,size+1):
    print((symbol+" ")*size)
