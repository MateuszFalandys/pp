# zadanie dotyczące zwrotów z inwestycji:
a = 14000
b = 14000 * 1.4
c = 14000 * 1.4 - 1500
d = 1.12 * (14000 * 1.4 - 1500)

print("Inwestycja 14000 zł w kolejnych latach przynosiła wyniki:")
print("W pierwszym roku zwrot po zysku 14% - kwota na koniec roku:", b)
print("W drugim roku zwrot po stracie 1500 - kwota na koniec roku:", c)
print("W trzecim roku zwrot po zysku 12% - kwota na koniec roku:", round(d, 0))
g = round(d, 0)
print(type(g))
