#  Korzystając z napisanej wcześniej klasy Stack:
# • utwórz 3 stosy (3 obiekty klasy Stack),
# • połóż na pierwszym stosie kolejno liczby od 1 do 100,
# • ściągaj kolejne elementy (liczby) z pierwszego stosu i umieszczaj na drugim,
# • ściągaj kolejne elementy z drugiego stosu i umieszczaj na trzecim,
# • ściągaj i wyświetlaj w tej samej linii elementy z trzeciego stosu.

class Stack:  #definicja klasy stosu
    def __init__(self): #definiujemy konstruktor
        self.__stack_list = []

    def push(self,val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

    def size(self):
        return len(self.__stack_list)

    def show(self):
        print(self.__stack_list)
        pass

object1=Stack()
object2=Stack()
object3=Stack()

for i in range(1,101):
    object1.push(i)

print("Stos pierwszy", object1.show(), end="")
print("Stos drugi", object2.show(), end="")
print("Stos trzeci", object3.show(), end="")

for i in range(1,101):
    object2.push(object1.pop())

print("Stos pierwszy", object1.show(), end="")
print("Stos drugi", object2.show(), end="")
print("Stos trzeci", object3.show(), end="")

for i in range(1,101):
    object3.push(object2.pop())

print("Stos pierwszy", object1.show(), end="")
print("Stos drugi", object2.show(), end="")
print("Stos trzeci", object3.show(), end="")
