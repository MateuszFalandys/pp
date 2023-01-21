znak = input("Wskaż znak z jakiego chcesz wygenerować figurę: \n")
il_kolumn = int(input("Wskaż ilość kolumn: \n"))
il_wierszy = int(input("Wskaż ilość wierszy \n"))
print((znak*il_kolumn + "\n")*il_wierszy, end="")