import math

class Animal:

    alive = True

    def eat(self):
        print("Animal is eating")

    def sleep(self):
        print("Animal is sleaping")

class Rabbit(Animal): #This is an example of inheritance, parent class is passed to the rabbit class.
    pass

class Fish(Animal):
    pass

class Hawk(Animal): 
    pass

# Creating objects
rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive) # Alive class variable is passed from the parent class - Animal
fish.eat()
hawk.sleep()

# Task:
class Shape:

    def square_perimeter(self, side):
        print(side*4)
    
    def square_area(self, side):
        print(side**2)
    
    def rect_perimeter(self, side1, side2):
        print((side1 + side2) * 2)
    
    def rect_area(self, side1, side2):
        print(side1 * side2)
    
    def circle_perimeter(self, radius):
        print(math.pi * 2 * radius)
    
    def circle_area(self, radius):
        print(math.pi * (radius**2))
    
class Square1(Shape):
    def __init__(self, side):
        self.side = side

class Rect1(Shape):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

class Circ1(Shape):
    def __init__(self, radius):
        self.radius = radius

square_instance = Square1(5)
rect_instance = Rect1(10, 5)
circ_instance = Circ1(10)

square_instance.square_perimeter(square_instance.side)
square_instance.square_area(square_instance.side)

rect_instance.rect_perimeter(rect_instance.side1, rect_instance.side2)
rect_instance.rect_area(rect_instance.side1, rect_instance.side2)

circ_instance.circle_perimeter(circ_instance.radius)
circ_instance.circle_area(circ_instance.radius)


# Task2:
class Car:

    def wheels():
        print("Has 4 wheels")

    def doors():
        print("Has 2 doors")

class e92(Car): # An example of inheritance
    def engine():
        print("Has N54 v8 engine")

class e30(Car):
    def year():
        print("Was released in 1990")

e92.engine()
e92.doors()
e30.year()
e30.wheels()