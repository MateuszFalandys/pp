# Napisz skrypt, pobierający od użytkownika zbiór imion, w tym celu:
# • skrypt powinien zapytać użytkownika o liczbę elementów zbioru,
# • pobrać kolejne elementy i zapisać je do listy,
# • wyświetlić w podsumowaniu jakie imiona pobrał od użytkownika.

a = int(input("Jaką liczbę imion chcesz umieścić w zbiorze?"))
names = []
for i in range(1,a+1):
    a = input("Podaj imię:")
    names.append(a)
print("Pobrane imiona to: ",names)