#+	Addition	x + y	
#-	Subtraction	x - y	
#*	Multiplication	x * y	
#/	Division	x / y	
#%	Modulus	x % y	
#**	Exponentiation	x ** y	
#//	Floor division	x // y
#the floor division // rounds the result down to the nearest whole number


#Assignment operators are used to assign values to variables:
#=	x = 5	x = 5	
#+=	x += 3	x = x + 3	
#-=	x -= 3	x = x - 3	
#*=	x *= 3	x = x * 3	
#/=	x /= 3	x = x / 3

x=7
print((x) * (4**3))
print(1230*43+5000)


list1 = ["python ", "javascript ", "html "]
list2 = ["13", "6"]
print(len(list1))
print(len(list2))
list3 = ("abc", 34, True, 40, "male")
print(list3)

mylist = ["apple", "banana", "cherry"]
print(type(mylist))
print(mylist[1])
#The first item has index 0.

#Print the last item of the list:
print(mylist[-1])


car_list = ["bmw", "audi", "nissan", "ferrari","ford", "honda", "toyota"]
#the first item is position 0, position 5 is NOT included
print(car_list[2:5])
print(car_list[:2])
print(car_list[4:])

car_list = ["bmw", "audi", "nissan", "ferrari","ford", "honda", "toyota"]
if "bmw" in car_list:
    print("bmw is in car list")
else:
    print("bmw is not in car list")

car_list[0]="mercedes"
print(car_list)
car_list[1:3] = ["general motors", "subaru"]
print(car_list)

thislist = ["apple", "banana", "cherry"]
thislist.insert(0, "peach")
print(thislist) 