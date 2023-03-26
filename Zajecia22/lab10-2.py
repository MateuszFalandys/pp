# Napisz program, który zasymuluje 16 rzutów kostką do gry a następnie
# wyświetli poniższe informacje:
# • zestaw wylosowanych wyników,
# • wyrzucaną wartość za 8 razem,
# • liczbę wyrzuconych szóstek,
# • maksymalną liczbę wyrzuconych tych samych wartości pod rząd.
import random

count = 0
maxi = []
t = []
maxim = 0
for i in range(16):
    a = random.randint(1, 6)
    t.append(a)
    if a == 6:
        count += 1
    if a == t[i - 1]:
        maxim += 1
        maxi.append(maxim)
    else:
        maxim = 1
        maxi.append(maxim)
max_result = max(maxi)
print("Wylosowane przez", len(t), "rzutów liczby to", t)
print("Szóśtek wyrzucono: ", count)
print("W ósmym rzucie wyrzucono: ", t[8 - 1])
print("Najwięcej razy ta sama liczba pod rząd wypadła:", max_result)
