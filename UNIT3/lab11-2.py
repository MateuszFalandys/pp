# Napisz skrypt pobierający od użytkownika serię liczb całkowitych, a
# następnie wyświetl je w kolejności malejącej pozbywając się wcześniej
# duplikatów.

count_number = int(input("Podaj ile liczb chcesz podać i posegregować:"))
selected_numbers = []
for i in range(count_number):
    selected_numbers.append(int(input("Podaj " + str(i+1) + " liczbę zbioru:")))

numbers_without_duplicate = []
for number in selected_numbers:
   if number not in numbers_without_duplicate:
       numbers_without_duplicate.append(number)



selected_numbers.sort(reverse=True)
print(numbers_without_duplicate)