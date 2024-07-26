#a = 10
#b = 20
#c = 1 + b
#for i in range(10):
#    print(c)


from turtle import *
speed(100)
#1st
for i in range(4):
    forward(100)
    left(90)
penup()
goto(0,200)
pendown()
#2nd
for i in range(4):
    forward(100)
    left(90)
penup()
goto(-200,200)
pendown()
#3rd
for i in range(4):
    forward(100)
    left(90)
penup()
goto(-200,0)
pendown()
#4th
for i in range(4):
    forward(100)
    left(90)

from turtle import * 

def draw_square():
    for i in range(4):
        forward(100)
        left(90)

def kalmis_wageba(x,y):
    penup()
    goto(x,y)
    pendown() 

draw_square()
kalmis_wageba(0,200)

draw_square()
kalmis_wageba(-200,200)

#third square
draw_square()
kalmis_wageba(-200,0)

#fourth square
draw_square()

exitonclick()


