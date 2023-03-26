def recursion(number):
    if number==20:
        return
    print(number, "x ", recursion(number))
    number +=1
    recursion(number)


recursion(10)