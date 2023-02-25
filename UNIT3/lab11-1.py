# Napisz skrypt symulujący grę losową:
# • użytkownik obstawia 6 liczb z 49,
# • program losuje 6 liczb z 49,
# • użytkownik dostaje informacje o ilości trafień.
import random

numbers = [i for i in range(1,50)]
selected_numbers = random.sample(numbers,6)
chosen_numbers = []
for i in range(1,7):
        chosen_numbers.append(int(input("Podaj " + str(i) + " liczbe. w zakresie od 1 do 49:   ")))
        if chosen_numbers[i-1]>49 or chosen_numbers[i-1]<1:
            chosen_numbers[i-1] = int(input("Liczba nie mie sci się w zakresie! podaj ją jeszcze raz:   "))
chosen_numbers.sort()
print("wybrane liczby to: ", chosen_numbers)
selected_numbers.sort()
print("Wylosowane liczby to:", selected_numbers)
count=0
for j in range(6):
    for i in range(6):
        if chosen_numbers[j] == selected_numbers[i]:
            count+=1
print("Liczba poprawnych trafień : ", count)

