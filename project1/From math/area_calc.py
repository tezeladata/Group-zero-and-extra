import math
print("Hello, this code helps you find area of geometrical figures!")
print("You can find area of: triangle, rectangle, paralellogram, trapezoid or circle.")
choice=input("Which geometrical figure's area do you want to find: ")
if choice=="triangle":
    base=float(input("The base of triangle is: "))
    height=float(input("The height of triangle is: "))
    triangle_area=0.5*base*height
    print("Area of your triangle with the base of {} and height of {} is {}.".format(base, height, triangle_area))
elif choice=="rectangle":
    length=float(input("The length of rectangle is: "))
    width=float(input("The width of rectangle is: "))
    rectangle_area=length*width
    print("Area of your rectangle with the length of {} and width of {} is {}.".format(length, width, rectangle_area))
elif choice=="paralellogram":
    base=float(input("The base of paralellogram is: "))
    height=float(input("The height of paralellogram is: "))
    paralellogram_area=base*height
    print("Area of your paralellogram with the base of {} and height of {} is {}.".format(base, height, paralellogram_area))
elif choice=="trapezoid":
    base1=float(input("The base one of trapezoid is: "))
    base2=float(input("The base two of trapezoid is: "))
    height=float(input("The height of trapezoid is: "))
    trapezoid_area=0.5*(base1+base2)*height
    print("Area of your trapezoid with the base one of {}, base two of {} and height of {} is {}.".format(base1, base2, height, trapezoid_area))
elif choice=="circle":
    radius=float(input("The radius of circle is: "))
    circle_area=math.pi*(radius**2)
    print("Area of your circle with the radius of {} is {}.".format(radius, circle_area))
else:
    print("Incorrect figure")
print("Thanks for attention!")