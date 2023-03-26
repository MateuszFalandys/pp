class MyClass:
    __counter = 0   #zmienna klasy - wspólna dla całej klasy obiektów
    def __init__(self, x=1):
        self.__x = x  #prywatna zmienna instancji
        MyClass.__counter +=1

obj1 = MyClass(1)
obj2 = MyClass(77)
obj3 = MyClass(3)

MyClass(3)
MyClass(3)

print("Ile obiketów?: ", MyClass._MyClass__counter)
print(obj1.__dict__,obj1._MyClass__counter)
print(obj2.__dict__,obj2._MyClass__counter)
print(obj3.__dict__,MyClass._MyClass__counter)

print(MyClass.__dict__)