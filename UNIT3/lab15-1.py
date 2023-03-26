#  Utwórz funkcję o nazwie safe_int(), która pobiera pojedynczy argument arg.
# Jeśli to możliwe, funkcja powinna przekonwertować podany argument na typ int
# i zwrócić go. Jeśli jednak nie jest to możliwe (tj. jeśli wystąpi wyjątek), funkcja
# powinna zwrócić None.

def safe_int():
    try:
        arg = int(input("Podaj argument:"))
        print("Twój argument po konwersji na int to:",arg)
    except:
        print("None")

while True:
    safe_int()