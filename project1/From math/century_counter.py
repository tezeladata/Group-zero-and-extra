print("Hello, this code calculates century from year!")
def century_counter(year):
    century=(year+99) // 100 # // operator is used for floor division
    print("Century for year", year, "is {}.".format(century))
century_counter(year=int(input("Enter year to calculate century: ")))
print("Thanks for attention!")