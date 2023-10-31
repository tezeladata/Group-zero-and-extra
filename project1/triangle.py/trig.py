import math
print("Hello, this code calculates sin/cos/tan for specified angle of a right triangle")
print("Note that C angle is a right angle")
AC=int(input("Value of cathetus AC: "))
BC=int(input("Value of cathetus BC: "))
hipotenuse=math.sqrt((AC**2)+(BC**2))
print("Value of hipotenuse is:", hipotenuse)
angle=input("Which angle do you choose: A/B - ")
if angle=="A" or angle=="a":
    operation=input("Which operation: sin/cos/tan - ")
    if operation=="sin":
        sin=BC/hipotenuse
        print("Sin(A) is:", sin)
    elif operation=="cos":
        cos=AC/hipotenuse
        print("Cos(A) is:", cos)
    elif operation=="tan":
        tan=BC/AC
        print("Tan(A) is:", tan)

if angle=="B" or angle=="b":
    operation=input("Which operation: sin/cos/tan - ")
    if operation=="sin":
        sin=AC/hipotenuse
        print("Sin(B) is:", sin)
    elif operation=="cos":
        cos=BC/hipotenuse
        print("Cos(B) is:", cos)
    elif operation=="tan":
        tan=AC/BC
        print("Tan(B) is:", tan)

print("Thanks for attention!")