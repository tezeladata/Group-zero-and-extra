# Multi-level inheritance - Dog class inherits from Animal, but Animal inherits fro Organism

class Organism:

    alive = True

class Animal(Organism):

    def eat(aelf):
        print("This animal is eating")

class Dog(Animal):

    def bark(self):
        print("This dog is barking")

dog1 = Dog()
print(dog1.alive)
dog1.eat()
dog1.bark()


# Task1:
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors, fuel_type):
        super().__init__(make, model, year)
        self.num_doors = num_doors
        self.fuel_type = fuel_type

    def display_info(self):
        super().display_info()  # Call display_info method of superclass
        print(f"Number of doors: {self.num_doors}, Fuel type: {self.fuel_type}")

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_size, top_speed):
        super().__init__(make, model, year)
        self.engine_size = engine_size
        self.top_speed = top_speed

    def display_info(self):
        super().display_info()  # Call display_info method of superclass
        print(f"Engine size: {self.engine_size}, Top speed: {self.top_speed}")

class ElectricCar(Car):
    def __init__(self, make, model, year, num_doors, fuel_type, battery_capacity):
        super().__init__(make, model, year, num_doors, fuel_type)
        self.battery_capacity = battery_capacity

    def display_info(self):
        super().display_info()  # Call display_info method of superclass
        print(f"Battery capacity: {self.battery_capacity}")

# Creating an instance of ElectricCar and displaying its information
el_car1 = ElectricCar("Tesla", "notacar1", 2022, 4, "electric", "5h")
el_car1.display_info()