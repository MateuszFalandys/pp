class MyClass:
    def __init__(self, x=1):
        self.__x = x  #prywatna zmienna instancji

    def sety(self, y):
        self.__y = y


obj1 = MyClass()
obj2 = MyClass(4)
obj2.sety(7)
obj3 = MyClass(3)
obj3.z = 99

print(obj1.__dict__)
print(obj2.__dict__)
print(obj3.__dict__)
