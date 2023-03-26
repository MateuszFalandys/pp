while True:
    try:
        number = int(input("Podaj liczbę całkowitą: "))
        print("Odwrotna liczba to:", 1 / number)
    except ZeroDivisionError:
        print("Błąd dzielenia przez 0.")
    except ValueError:
        print("To nie jest liczba całkowita!")
    except:
        print("Coś posszło nie tak...!")

