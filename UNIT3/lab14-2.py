# Napisz funkcje zamieniającą 3 listy na 1 krotkę bez powtarzających się elementów.
# Przykład: [1, 2], [1, 1], [4, 4, 4] -> (1, 2, 4)

def converter_list(a,b,c):
    print(a,b,c)
    list_sum = a+b+c
    print(list_sum)
    list_tuplets=[]
    for i in list_sum:
        if i not in list_tuplets:
            list_tuplets.append(i)
    list_tuplets=tuple(list_tuplets)
    print("Utworzona krotka to:",list_tuplets)


converter_list([1,2],[1,1],[4,4,4])
