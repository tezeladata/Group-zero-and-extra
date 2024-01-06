print("This code calculates area of biggest square in circle, by circle radius.")
def square_area(r):
    square_side=(r**2 + r**2)**0.5
    return "Biggest square's area in circle with radius of {} is {}".format(r, square_side**2)
print(square_area(r=(float(input("Enter radius of circle: ")))))