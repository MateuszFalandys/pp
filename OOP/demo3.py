class MyClass:
    def __init__(self, x=1):
        if x%2 ==0:
            self.a = x
        else:
            self.b = x

obj = MyClass(23)
print(obj.__dict__)

if (hasattr(obj, "a")):
    print(obj.a)
else:
    print(obj.b)