# function calls inside cther function calls
# innermost function calls are resolved first
# returned value is used as argument for the next outer function

# Bad way:
# user_num = (input("Enter number: "))
# user_num = float(user_num)
# user_num = abs(user_num)
# user_num = round(user_num)
# print(user_num)

# Better way:
# print(round(abs(float(input("Enter number here: ")))))

# Task:
def main_func(number, function):
    return f"Factorial for {number} is {function(number)}"

def calculate_factorial(number):
    fact = 1
    for i in range(2, number+1):
        fact *= i
    return fact

print(main_func(function=calculate_factorial, number=int(input("Enter integer here: "))))