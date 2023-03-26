###############################
# operatory bitowe

a = 5
b = 2

for i in range(5, -6, 1):
    print("{0:08b} =>{1:d}".format(i & 255, i))

# negacja bitowa
print("~", a, "=", ~a)
print("{:08b}".format(a))
print("-" * 8)
print("{:08b}".format(~a))

# alternatywa bitowa przesunięcie
print(a, "<<", b, "=", a << b)
print("{:08b}".format(a))
print("-" * 8)
print("{:08b}".format(a << b))

# alternatywa bitowa przesunięcie
print(a, ">>", b, "=", a >> b)
print("{:08b}".format(a))
print("-" * 8)
print("{:08b}".format(a >> b))

# alternatywa bez koniunkcji bitowa
print(a, "^", b, "=", a ^ b)
print("{:08b}".format(a))
print("{:08b}".format(b))
print("-" * 8)
print("{:08b}".format(a ^ b))

# alternatywa bitowa
print(a, "|", b, "=", a | b)
print("{:08b}".format(a))
print("{:08b}".format(b))
print("-" * 8)
print("{:08b}".format(a | b))

# koniunkcja bitowa
print(a, "&", b, "=", a & b)
print("{:08b}".format(a))
print("{:08b}".format(b))
print("-" * 8)
print("{:08b}".format(a & b))
