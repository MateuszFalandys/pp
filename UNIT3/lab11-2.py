# Napisz skrypt pobierający od użytkownika serię liczb całkowitych, a
# następnie wyświetl je w kolejności malejącej pozbywając się wcześniej
# duplikatów.

count_number = int(input("Podaj ile liczb chcesz podać i posegregować:"))
selected_numbers = []
for i in range(count_number):
    selected_numbers.append(int(input("Podaj numer:")))

for i in range(count_number):
    for j in range(count_number):
        if selected_numbers[i] == selected_numbers[j]:
            selected_numbers.remove(i)

selected_numbers.sort(reverse=True)
print(selected_numbers)