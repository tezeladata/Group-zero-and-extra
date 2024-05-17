# parameter that will pack all arguments into a dicltionary
# useful so that a function can accept a varying amount of keyword arguments

# def hello(first, last):
#     print("Hello " + first + " " + last)
# hello("David", "Tezelashvili")

# Using kwargs:
# def better_hello(**kwargs):
#     # print(f"Hello {kwargs['first']} {kwargs['middle']} {kwargs['last']}")

#     print("Hello", end=" ")
#     for key,value in kwargs.items():
#         print(value, end=" ")

# better_hello(first="James", middle="Johnson", last="III")


# Task:
def total_price(**kwargs):
    total_price = 0
    for key, value in kwargs.items():
        total_price += value
        print(f"{key} - {value}", end=" | ")
    print(f"Total price of your items is: {total_price}")


total_price(banana = 15, apple = 10, bread = 5)