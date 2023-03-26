#  Rozbuduj klasę Employee o mechanizm zwiększania wynagrodzeń:
# • dodaj metodę risesalary(),
# • metoda powinna zwiększać zarobki o podaną wartość procentową,
# • domyślnie metoda powinną zwiększać zarobkio 10%.

class Employee:
    def __init__(self, firstname, lastname, age, salary, rise=0.1):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__age = age
        self.__salary = salary
        self.__rise = rise

    def getsalary(self):
        return self.__salary

    def getfullname(self):
        return self.__firstname +  " " + self.__lastname

    def getage(self):
        return self.__age

    def rise(self):
        return self.__rise

    def risesalary(self):
        return self.__salary * (1+self.__rise)

employees = []
employees.append(Employee("Jan","Kowalska",25,3800,0.2))
employees.append(Employee("Bartosz","Kul",30,4800,0.1))
employees.append(Employee("Dawid","Bortniczuk",50,5800))

print("Lista płac:")
print("-"*50)

for e in employees:
    print(e.getfullname(), "wiek: ", e.getage(), "lat. Zarobki przed podwyżką: ", e.getsalary(), "zł. A po podwyżce o ",e.rise()*100, "% zarobki wyniosą", e.risesalary())