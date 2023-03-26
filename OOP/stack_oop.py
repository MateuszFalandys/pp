#programowanie obiektowe

class Stack:  #definicja klasy stosu
    def __init__(self): #definiujemy konstruktor
        self.__stack_list = []

    def push(self,val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

class StackSum(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum=0

    def get_sum(self,val):
        return self.__sum

    def push(self,val):
        self.__sum += val
        Stack.push
# class Stack:  #definicja klasy stosu
#     def __init__(self): #definiujemy konstruktor
#         self.__stack_list = []     enkapsulacja - nie wolno modyfikowa c tego elementu.

obj = StackSum()
obj2 = StackSum()

obj.push(3)
obj.push(2)
obj.push(1)
print(obj)
print(obj.pop())
print(obj)
print(obj.pop())
print(obj)
print(obj.pop())

obj2.push(4)
obj2.push(4)
obj2.push(4)