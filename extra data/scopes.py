# The region that a variable is recognized
# A variable is only available from inside the region it is created.
# A global and locally scoped versions of a variable can be created

def func1():
    name = "David"
    print(name)
func1()
# print(name) Error because name has local scope and is only available inside function

# Function first searches for local scope and if not available, uses global one.

name = "Andria"
def func2():
    name = "David"
    print(name)
func2() # Local scope this time

def func3():
    print(name)
func3() # Global scope this time

# Global scope is variable, that is available everywhere

# Task:
def outer_func():
    outer_var = 10

    def inner_func():
        inner_var = 20
        nonlocal nonlocal_var
        return inner_var, outer_var, nonlocal_var
    
    nonlocal_var = nonlocal_func()
    return inner_func(), outer_var, nonlocal_var

def nonlocal_func():
    nonlocal_var = 30
    return nonlocal_var

print(outer_func())