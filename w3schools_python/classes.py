#Almost everything in Python is an object, with its properties and methods.
#A Class is like an object constructor, or a "blueprint" for creating objects.
class Mynumbers:
    numbers=[]
    for x in range(2, 100, 7):
        numbers.append(x)

print(Mynumbers)

class greet:
    a="Hello"
    b="Hallo"
h1=greet()
h2=greet()
print(h1.a, h2.b)

class car:
    def __init__(self, brand, model, year):
        self.brand=brand
        self.model=model
        self.year=year
    def year_func(self):
        print("Bmw Nazca was made in", self.year)
car1=car("Bmw", "Nazca M12", 1991)
car1.year_func()


class element:
    def __init__(chemistry, name, discovery_year):
        chemistry.name=name
        chemistry.discovery_year=discovery_year
    def func1(chemistry):
        print("Element is " + chemistry.name)
        print("Discovery year is", chemistry.discovery_year)
element1=element("Chlorine", 1774)
element2=element("Fluorine", 1886)
element1.func1()
element2.func1()

#modifying parameter of element:
element1.name="Iodine"
element1.year=1811
element1.func1()

#deleting parameter:
# del element1.name
# element1.func1() error because not enough parameters

#deleting object:
# del element1
# element1.func1() error because there is not element1 and we are calling it

#using pass for nothing:
class element:
    pass