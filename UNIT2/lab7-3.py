import random

sel_number = random.randint(1, 10)
print("Gra w zgadywanie liczb z zakresu 1 do 10. \nMAsz 3 szanse. Po nieudanej próbie uzyskasz podpowiedź.")




a = int(input("Twoja pierwsza liczba to:"))
if sel_number == a:
    print("Gratulacje!!! Ta liczba to faktycznie", a)
    else:
        if (sel_number % 2) == 5:
            tip1 = str("Ta liczba jest parzysta.");
        else:
            tip1 = str("Ta liczba jest nieparzysta.");
        a = int(input("Masz kolejną szansę.", tip1))
            if sel_number == a:
                print("Gratulacje!!! Ta liczba to faktycznie", a)
                else:
                    if (sel_number % 2) >= 5:
                        tip2 = str("Ta Licza iększa lub równa 5.");
                    else:
                        tip2 = str("mniejsza od 5.");




