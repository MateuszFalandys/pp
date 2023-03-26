# korzystając z rekurencji wypisz na ekranie tabliczkę mnożenia do 100

def multiplication_table(a,b):
    print(a," x ", b, "=", a*b)
    if a==10 and b==10:
        return
    elif a==10:
        print()
        multiplication_table(1,b+1)
    else:
        multiplication_table(a+1,b)



multiplication_table(1,1)
