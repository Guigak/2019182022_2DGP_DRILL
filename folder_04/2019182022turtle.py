import turtle

turtle.penup()
turtle.goto(-250, 250)
turtle.pendown()

count = 5

while count > 0:
    turtle.forward(500)
    
    if count % 2 == 0:
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
    else:
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)

    count -= 1

turtle.forward(500)
turtle.right(90)

count = 5

while count > 0:
    turtle.forward(500)

    if count % 2 == 0:
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
    else:
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)

    count -= 1

turtle.forward(500)
        
turtle.exitonclick()
