# Wyświetl liczby od 1 do 100 z pominięciem liczb podzielnych przez 3.

for i in range(1,100+1):
    if i%3==0:
        print("", end="")
    else:
        print(i, end=" ")
    i+=1
