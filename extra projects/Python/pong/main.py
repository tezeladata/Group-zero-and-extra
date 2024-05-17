import turtle
import winsound

# Adding window
wn = turtle.Screen()

# Title of window
wn.title("Pong game by David")

# Customization
wn.bgcolor("green")
wn.setup(width=800, height=600)
wn.tracer(0)

# Scores
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle() # Turtle object
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
# Changing size
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
# Not leaving lines when moving
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle() 
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle() 
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
# on every loop, ball moves by 0.02 pixels:
ball.dx = 0.02
ball.dy = 0.02

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "italic"))


# functions for paddle moving
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    # When moving up, 20 pixels are added
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    # When moving down, 20 pixels are removed
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Main logic
while True:
    # Every time loop runs, window updates
    wn.update()

    # Moving the ball
    ball.setx(ball.xcor() + ball.dx) # 0.02 pixels
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    # Top
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        # Sound
        winsound.PlaySound("pong.wav", winsound.SND_ASYNC)

    # Bottom
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        # Sound
        winsound.PlaySound("pong.wav", winsound.SND_ASYNC)

    # Right
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        # player1 score
        score_a += 1

        # Sound
        winsound.PlaySound("lose.wav", winsound.SND_ASYNC)

        # Total score
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "italic"))

    # Left
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        # player2 score
        score_b += 1

        # Sound
        winsound.PlaySound("lose.wav", winsound.SND_ASYNC)

        # Total score
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "italic"))


    # Collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        # Sound
        winsound.PlaySound("pong.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        # Sound
        winsound.PlaySound("pong.wav", winsound.SND_ASYNC)