#####################################
# Badanie boków trójkąta
print("Podaj długości 3 odcinków - liczby całkowite:")
a = int(input("Podaj a:"))
b = int(input("Podaj b:"))
c = int(input("Podaj c:"))
if (a + b) > c and (a + c) > b and (b + c) > a:
    print("Z tych odcinków można zbudować trójkąt.")
    d = max(a, b, c)
    print("Wartośc maksymalnego boku to: ", d)
    if a == b and b == c and c == a:
        print("Trójkąt jest równoboczny.")
    elif a == b or b == c or c == a:
        print("Trójkąt jest równoboczny.")
    else:
        print("Trójkąt nie jest ani równoboczny, ani równormaienny")
    if a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or a ** 2 + c ** 2 == b ** 2:
        print("Trójkąt jest prostokątny")
    elif a ** 2 + b ** 2 < c ** 2 or b ** 2 + c ** 2 < a ** 2 or a ** 2 + c ** 2 < b ** 2:
        print("Trójkąt jest Rozwartokątny:")
    else:
        print("Trójkąt jest ostrokątny!")
else:
    print("niestety z tych odcinków NIE powstanie trójkąt.")

#####################################
# Zadanie z pętli i koniunkcji
# Wyświetlc cyfrę, chyba że: liczba parzysta lub liczba większa od 6 to wyświetl *
# for i in range(10):
#     if i % 2 == 0 or i > 6:
#         print("*")
#     else:
#         print(i)

#####################################
# Zadanie z zakresu łączenia warunków 2
# Jeżeli temperatura będzie ujemna lub będzie pochmurno - zostaniemy w domu,
# a jeżeli nie to spacer
# clear = False
# temperature = 55
# if temperature < 0 and not clear:
#     print("Zostaniemy w domu!")
# else:
#     print("Idziemy na spacer!")

#####################################
# Zadanie z zakresu łączenia warunków

# temperature = -5
# is_sun_shining = True
# zst = -1
# if (temperature > 0 or is_sun_shining) and zst > 0:
#     print("Idzemy na spacer!")
# else:
#     print("Trza zostać w domu")
