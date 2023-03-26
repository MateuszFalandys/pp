# Udowodnij, że w zbiorze liczb z zakresu 1-100, jest 11 liczb, które są
# parzyste i jednocześnie większe od 90, a gdy są nieparzyste, to
# przynajmniej dzielą się przez 9.

count = 0
for i in range(1, 100 + 1):
    if not i % 2 == 0 and i % 9 == 0:
        count += 1
        print(i, end=" ")
    if i % 2 == 0 and i > 90:
        count += 1
        print(i, end=" ")
print("")
print("Liczb jest ", count,
      " w zbiorze liczb z zakresu 1-100, które są parzyste i jednocześnie większe od 90, a gdy są nieparzyste, to przynajmniej dzielą się przez 9")
