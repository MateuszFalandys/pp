# #Napisz skrypt wyznaczający ocenę jaką otrzyma student, ze względu na ilość
# otrzymanych punków z kolokwium:
# • ocena bardzo (5,0) dobra, jeżeli student otrzymał 95 lub więcej punktów,
# • jeżeli punktów jest mniej niż 95, ale więcej niż 84 studentowi przysługuje ocena ponad dobra
# (4,5),
# • ocena dobra (4,0) przyznawana jest dla ilości punktów z przedziału [70, 84],
# • jeżeli student otrzymał więcej niż 60 ale mniej niż 70 to przysługuje mu ocena dość dobra
# (3,5),
# • ocena dostateczna jest dla studentów z punktowym wynikiem równym przynajmniej 60 ale
# powyżej 50 punktów,
# • wszystkie wyniki równe 50 i mniej punktów wiążą się z otrzymaniem oceny niedostatecznej
# (2.0).

print("Skrypt określi ocenę ucznia w zależności od ilości uzyskanych punktów.")
ocena = int(input("Podaj ilość punktów zdobytą przez ucznia: "))
if ocena >= 95:
    print("Należy wystawić ocenę 5,0")
elif ocena >= 85:
    print("Należy wystawić ocenę 4,5")
elif ocena >= 70:
    print("Należy wystawić ocenę 4,0")
elif ocena >= 61:
    print("Należy wystawić ocenę 3,5")
elif ocena >= 51:
    print("Należy wystawić ocenę 3,0")
else:
    print("Egzamin oblany - ocena 2,0")
