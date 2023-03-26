import random
numbers = []

for i in range(10):
    number = random.randint(1,100)
    numbers.append(number)
print(numbers)

fruits=["banan","jabłko","wiśnie"]
for n in range(len(fruits)):
    print(n, fruits[n])

for f in fruits:
    print(f)