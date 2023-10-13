from turtle import *
#building a house
speed(30)
#square
width(7)
color("purple")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)

#door
forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()
#roof
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#windows
penup()
goto(30, 140)
pendown()

color("brown")
begin_fill()
right(150)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()

penup()
goto(130, 140)
pendown()

color("brown")
begin_fill()
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()












exitonclick()