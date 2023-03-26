# Napisz program wyznaczający wartość n-tego bitu dla dowolnej liczby
# całkowitej. Bity liczymy od 0, od najmniej znaczącego bitu.
number = int(input("Podaj wartość dowolnej liczby całkowitej:"))
print(number, "  ->  ", bin(number), "  ->  ", "{:040b}".format(number))  # wartość binarna
count = int(input("Którą wartośc n-tego bitu mam wyświetlić?"))
# 0 1 1 0 0
# 0 0 0 0 1 - maska
# &
# 0 0 0 0 1 - koniunkcja bitowa
mask = 1 << count
result = number & mask
bit = int(bool(result))
print("Bit na pozycji ", count, " dla liczby ", number, "wynosi", bit)
