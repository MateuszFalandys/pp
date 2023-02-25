a = 1
b = 2
print("a =", a, "b =", b)
a, b = b, a
print("a =", a, "b =", b)

numbers =[1, 2 ,3]
numbers[0], numbers[1] = numbers[1], numbers[0]
print(numbers)
