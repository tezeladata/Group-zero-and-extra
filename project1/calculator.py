print("Your numbers are:")
x = float(input("First number = "))
y = float(input("Second number/Degree = "))

print("Select operation:")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print("5. Exponentiation/root")
choice = input("1/2/3/4/5 - ")

if choice == "1":
    print(x+y)
elif choice == "2":
    print(x-y)
elif choice == "3":
    print(x*y)
elif choice == "4":
    print(x/y)
elif choice == "5":
    print(x**y)
else:
    print("Incorrect data")

print("Thanks for attention")