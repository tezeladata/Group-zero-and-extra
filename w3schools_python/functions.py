# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.
def greet():
    print("hello")
greet()

#arguments
def whole_name(first_name, last_name):
    print("{}.{}".format(first_name[0], last_name[0]))
whole_name("David", "Tezelashvili")

#If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
def whole_name(*first_name):
    print(first_name)
whole_name("David", "Andria")

#You can also send arguments with the key = value syntax.
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#Passing a List as an Argument
def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)