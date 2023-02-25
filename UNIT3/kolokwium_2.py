# #Napisz program, który w zbiorze liczb całkowitych od 1 do 100, znajdzie i wypisze na ekran wszystkie liczby nieparzyste i jednocześnie podzielne prez 7.
#
# for i in range(1,101):
#     if i % 2 != 0 and i%7==0:
#         print(i)
#
# list = [i for i in range(100) if i % 2 != 0 and i%7==0]
# print(list)

a=4
b=9
c=[i for i in range(a,b+1)]
suma = sum(c)

print(suma)