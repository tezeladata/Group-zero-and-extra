old_list = [2,4,1,6,8,1]
# new_list = set(old_list)
# print(new_list)
old_list = [2,4,1,6,8,1]
new_list = []
for num in old_list:
    if num != 4:
        new_list.append(num)
print(new_list)

a = "{x}, {y}".format(x=5, y=12)
print(a)

x = ", ".join(["spam", "eggs", "ham"]) #ყველას მიეწერება ,
print(x)

str = "some text goes here"
x = str.split(' ')
print(x)

x = "Hello ME"
print(x.replace("ME", "world")) #ME იცვლება world-ით

#keyword to create function
#square_area - name of function
#lenght_of_side - parameter of function
def square_area(lenght_of_side):
    print(lenght_of_side**2)
square_area(float(input()))

