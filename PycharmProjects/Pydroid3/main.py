import turtle
import random
import time
rl = ["right", "left"]
# Function to create a ball and set its properties
def create_ball(color):
    ball = turtle.Turtle()
    ball.shape("circle")
    ball.color(color)
    ball.speed(0)
    return ball
# Ask the user for a run time
el_time = int(input("How many seconds would you like the simulation to run for? "))
# Create a list of colors to use for the balls
colors = ["red", "orange","purple", "darkblue"]

# Create a list to hold the ball turtles
balls = []

# Create the balls and add them to the list
for color in colors:
    balls.append(create_ball(color))

# Define the movement of each ball
for ball in balls:
    ball.penup()
    ball.goto(random.randint(-300, 300), random.randint(-300, 300))
    ball.pendown()
    ball.setheading(random.randint(0, 360))



# Start the timer
start_time = time.time()

# Run the simulation for the user-specified amount of time
turtle.clear()
turtle.bgcolor("white")
turtle.tracer(0,0)
while True:
    for ball in balls:
        ball.forward(5)
        ball.right(0.5)

        # Check for collision with the walls
        if ball.xcor() > 300:
            ball.goto(300, ball.ycor())
            ball.setheading(random.randint(1, 179))
        elif ball.xcor() < -300:
            ball.goto(-300, ball.ycor())
            ball.setheading(random.randint(181, 359))
        if ball.ycor() > 300:
            ball.goto(ball.xcor(), 300)
            ball.setheading(random.randint(89,269))
        elif ball.ycor() < -300:
            ball.goto(ball.xcor(), -300)
            ball.setheading(random.randint(0, 89))

        # Check for collision with other balls
        for other_ball in balls:
            if other_ball != ball and abs(ball.distance(other_ball)) < 30:
                ball.setheading((ball.heading()+random.randrange(135,225)))
                other_ball.setheading((ball.heading()+random.randrange(135,225)))



    turtle.update()
    # Check if the specified amount of time has elapsed
    if time.time() - start_time > el_time:
        turtle.done()
        break
