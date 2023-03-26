def change_value(n):
    print("przed zmianą:", n)
    n = [0,0]
    print("po zmianie:", n)


val = [1,2]
change_value(val)
print(val)

# -------------------------------------------------------
# def scope_test():
#     global x
#     x = 123
#     print("w środku funkcji:  " + str(x))
#
#
#
# scope_test()
# x = 99
# print("Na zewnątrz    " + str(x))

# -----------------------------------------------------
# import random
#
#
# def generate_numbers(total_numbers):
#     numbers = []
#     for i in  range(total_numbers):
#         numbers.append(random.randint(95, 99))
#     return numbers
#
# print(generate_numbers(10))
