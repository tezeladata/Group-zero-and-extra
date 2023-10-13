print(2!=3)

x=7
print(x!=3)
print(x>=7)
print("a" > "b")


x=(7>5)
print(int(x))

#1 - true, 0 - false
user_num = int(input("enter any number"))

if user_num>10:
    print("მეტია ათზე")
elif user_num==10:
    print("უდრის ათს")
else:
    print("ნაკლებია ან ტოლია ათის")

math = int(input("რა არის შენი სკოლის ნიშანი მათემატიკაში?"))
georgian = int(input("რა არის შენი სკოლის ნიშანი ქართულში?"))
english = int(input("რა არის შენი სკოლის ნიშანი ინგლისურში?"))
biology = int(input("რა არის შენი სკოლის ნიშანი ბიოლოგიაში?"))
geography = int(input("რა არის შენი სკოლის ნიშანი გეოგრაფიაში?"))
physics = int(input("რა არის შენი სკოლის ნიშანი ფიზიკაში?"))
history = int(input("რა არის შენი სკოლის ნიშანი ისტორიაში?"))
all=((math + georgian + english + biology + geography + physics + history) / 7)
if all>9:
    print("გილოცავ, მატრიცელო. შენი ქულაა " + str(all) + " შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რისთვისაც შეალიე შენი ცხოვრების წლები")
elif all<5:
    print("გილოცავ, შენი ქულაა " + str(all) + " შენ გაექეცი მატრიცას")
elif 5<all<9:
    print("YOU ARE MID, შენი ქულაა " + str(all) + "")
if all<0:
    print("there is something wrong with you")