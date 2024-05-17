# Instance variable is created inside constructor
# Class variables are declared within the class, but outside the constructor

class Car:

    wheels = 4 #class variable. it can be added to all of the objects
    # It more like global scope, than local one

    def __init__(self, make, model, year, color):
        self.make = make #instance variable
        self.model = model #instance variable
        self.year = year #instance variable
        self.color = color #instance variable

car1 = Car("Bmw", "e92", 2008, "Grey")

print(car1.wheels) # 4 is printed, because every object created in Car class has that variable

car1.wheels = 3
print(car1.wheels) # we can also change value of class variables

# We can also show example of class variable without creating an object:
print(Car.wheels)

# Changing class variable data outside the class:
Car.wheels = 1
# Eventually, objects will also have that value updated
print(car1.wheels)