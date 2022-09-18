import turtle

turtle.shape('turtle')
turtle.stamp()

def Go_Up():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def Go_Left():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def Go_Down():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()

def Go_Right():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

turtle.onkey(Go_Up, 'w')
turtle.onkey(Go_Left, 'a')
turtle.onkey(Go_Down, 's')
turtle.onkey(Go_Right, 'd')

turtle.listen()

turtle.exitonclick()
