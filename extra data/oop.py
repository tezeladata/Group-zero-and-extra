# We can create objects as we see in real life in python, by attributes and methods.

# Class tells us what attributes and methods out object has

# Attributes describe what an object is or has

# Class names should be capital
# This class is blueprint - a constructor for us, so we can create many objects from it
class Car:

    # We also need special thing called __init__ that will create some objects for us, in js it's called constructuor (probably same as this):
    def __init__(self, make, model, year, color):
        # Attributes:
        self.make = make # whatever we receive as "make" argument
        self.model = model
        self.year = year
        self.color = color
        # self is reffering to the object we are currently working on


    # Adding methods:
    def drive(self): #self refers to the object that is using this method (probably this in js)
        print(""+self.model+" is driving")
        #      "+self.attribure+" is correct way

    def stop(self):
        print(""+self.model+" has stopped")


# Now creating car objects:
# We do not have to pass self (car_1 in this case), because it is done automatically
car_1 = Car("Bmw", "e34", 1990, "Purple")

# Now accesing to some of the attributes:
print(car_1.make)
print(car_1.year)
print(car_1.model)
print(car_1.color)

# We use print inside this object's methods, so we only have to call method:
car_1.drive()
car_1.stop()

# Second car:
car_2 = Car("Nissan", "Silvia", 1995, "Silver")
print(car_2.make)
print(car_2.year)
print(car_2.model)
print(car_2.color)
car_2.drive()
car_2.stop()