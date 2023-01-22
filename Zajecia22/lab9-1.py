print("#Wyświetle tylko liczby podzielne przez 3, 5 lub 7, ze zbioru liczb z zakresu określonego przez użytkownika.")
a=int(input("Określ początkową liczbę całkowita zbioru: "))
b=int(input("Określ końcową liczbę całkowita zbioru: "))

for i in range(a,b+1):
    if i%3==0 or i%5==0 or i%7==0:
        print(i, end=" ")
    else:
        print("",end="")