# 1 1 2 3 5 8 13 21 44 65

def fib(n):
    if n<1:
        return None
    if n< 3:
        return 1
    el1 = el2 =1
    sum = 0
    for i in range(3,n+1):
        sum = el1+el2
        el1, el2 = el2, sum
    return sum

print(fib(5))

for n in range(1,10001):
    print(n,"  ->  ", fib(n))
    print()