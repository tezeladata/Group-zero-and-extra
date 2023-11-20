print("Hello, this is deposit calculator")
initial_amount = int(input("Money you will deposit is: "))
method = input("Select deposit method: simple/compound ")
percent = int(input("Percent: "))
time = (input("Money is on deposit for specified: months/years: "))

if time == "months" and method == "simple":
    month = int(input("How many months? "))
    simple1 = initial_amount * (1 + ((percent * month) / 100))
    print("Accumulated money in", month, "months will be", simple1, "gels!")
elif time == "months" and method == "compound":
    month = int(input("How many months? "))
    compound1 = initial_amount * ((1 + (percent / 100))**month)
    print("Accumulated money in", month, "months will be", compound1, "gels!")
elif time == "years" and method == "simple":
    year = int(input("How many years? "))
    simple2 = initial_amount * (1 + ((percent * year) / 100))
    print("Accumulated money in", year, "years will be", simple2, "gels!")
elif time == "years" and method == "compound":
    year = int(input("How many years? "))
    compound2 = initial_amount * ((1 + (percent / 100))**year)
    print("Accumulated money in", year, "years will be", compound2, "gels!")
else:
    print("Incorrect data")
print("Thanks for attention")