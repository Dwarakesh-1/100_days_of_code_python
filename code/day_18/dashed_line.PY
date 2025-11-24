from turtle import Turtle, Screen
  

timmy_the_turtle = Turtle()

for _ in range(15):
    timmy_the_turtle.fd(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.fd(10)
    timmy_the_turtle.pendown()


screen = Screen()
screen.exitonclick()
