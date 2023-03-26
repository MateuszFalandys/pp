# 1. Zaprojektuj klasę reprezentującą osobę (Person) wg założeń:
# • każdy obiekt tej klasy powinien posiadać właściwości: imię oraz wiek,
# • zabezpiecz właściwości obiektu przed przypadkowym nadpisaniem,
# • ustawienie odpowiednich właściwości obiektu powinno następować podczas jego tworzenia,
# • każdy obiekt tej klasy powinien móc wykonać akcję przedstawienia się.

class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def getname(self):
        return self.__name

    def getage(self):
        return self.__age

    def introduce(self):
        print("Cześć, jestem", self.__name, "I mam", self.__age, "lat/a.")

persons = []
persons.append(Person("Ala",28))
persons.append(Person("Ela",34))
persons.append(Person("Olak",23))

print("To jest lista osób:")
for e in persons:
    print(e.getname(), "wiek: ", e.getage())

