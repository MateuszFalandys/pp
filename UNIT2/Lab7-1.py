# Napisz skrypt sprawdzający czy pierwiastek kwadratowy z liczby całkowitej pobranej od użytkownika jest także liczbą całkowitą.
print("Skrypt sprawdzi czy pierwiastek kwadratowy z dowolnie wybranej liczby jest liczbą całkowitą.")
sel_number = int(input("Proszę podaj wybraną przez siebie liczbę całkowitą :"))
if ((sel_number ** .5) % 1) == 0:
    print("Pierwiastek z wybranej liczby jest liczbą całkowitą.")
else:
    print("Pierwiastek z wybranej liczby NIE jest liczbą całkowitą.")
