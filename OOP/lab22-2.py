# 2. Napisz klasę zliczającą wszystkie powstałe swoje instancje.

class MyClass:
    __counter = 0   #zmienna klasy - wspólna dla całej klasy obiektów
    def __init__(self, x=1,y=2,z=3):
        self.__x = x  #prywatna zmienna instancji
        self.__y = y
        self.__z = z
        MyClass.__counter += 1



obj1 = MyClass(1,2,3)
obj2 = MyClass(3)
obj3 = MyClass()
MyClass(2)
print("Ile obiketów?: ", MyClass._MyClass__counter)

