#Python has two primitive loop commands:
#while loops
#for loops


x=0
while x<=29:
    x+=1
    if x%2==0:
        print(str(x) + "ლუწი")
    else:
        print(str(x) + "კენტი")

x=int(input("your number: "))
y=20
if x/y > 360:
    print(str(x) + " მეტია 7200-ზე")

n=1
while n<4:
    n+=1
    print(n)
    if n==3:
        break

#With the continue statement we can stop the current iteration, and continue with the next:
x=60
while x<140:
    x+=20
    if x==100:
        continue
    print(x)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")