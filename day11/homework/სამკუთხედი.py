def triangle_checker(side1, side2, side3):
    if side1+side2>side3 and side1+side3>side2 and side2+side3>side1:
        print("Triangle is valid")
    else:
        print("Triangle is not valid")
triangle_checker(side1=float(input("First side: ")), side2=float(input("Second side: ")), side3=float(input("Third side: ")))