class myclass:
    i = 8
print(myclass)

#Now we can use the class named MyClass to create objects:
class myclass:
    x=13
x1=myclass
print(x1.x)

#The __init__() function is called automatically every time the class is being used to create a new object.
class car:
    def __init__(self, name, year):
        self.name=name
        self.year=year
c1 = car("bmw e46", 1998)
print(c1.name)
print(c1.year)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello, my name is " + self.name)

p1 = Person("David", 15)
p1.myfunc()
