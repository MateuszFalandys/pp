class MyClass:
    y=99
    def my_method(self,x):
        self.other_method()
        print("To jest moja metoda", x, "i zmienna klasy", self.y)

    def other_method(self):
        print("Too jest metoda ", self.y)


obj = MyClass()
obj.my_method(123)
obj.my_method("123")