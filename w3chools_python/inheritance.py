#Inheritance allows us to define a class that inherits all the methods and properties from another class.
class brand:
    def __init__(self, name, country, year):
        self.name = name
        self.country = country
        self.year = year
    def printname(self):
        print(self.name, self.country, self.year)
x = brand("Bmw", "Germany", "1916")
y = brand("Mercedes", "Germany", "1925")
x.printname()
y.printname()


class Person:
    def __init__(self, fname, lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname, self.lastname)
x = Person("David", "Tezelashvili")
x.printname()

#Now the Student class has the same properties and methods as the Person class.
class Student(Person):
  pass

x = Student ("John", "Stone")
x.printname()

#The __init__() function is called automatically every time the class is being used to create a new object.
class Student(Person):
    def __init__(self, fname, lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname, self.lastname)
x = Student("Steve", "Johnson")
x.printname()

#Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear=2015

x = Student("Mike", "Olsen")
print(x.graduationyear)

#we can add parameter called year
class Student(Person):
   def __init__(self, fname, lname, year):
      super().__init__(fname, lname)
      self.graduationyear = year
x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)

#methods
class Student(Person):
   def __init__(self, fname, lname, year):
      super().__init__(fname, lname)
      self.graduationyear = year
x = Student("George", "Smith", 2017)
print("Welcome", x.firstname, x.lastname, "to the class of", x.graduationyear)


#f.e class of element
class Element:
    def __init__(self, name, year):
        self.name = name
        self.year = year
    def printname(self):
        print(self.name, self.year)
x = Element("Potassium", 1807)
x.printname()

