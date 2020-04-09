import turtle
number=int(input("please input:"))

turtle.bgcolor("black")

turtle.color("yellow")
for x in range(number):
    turtle.circle(30)
    turtle.left(360/number)
turtle.color("red")
for x in range(number):
    turtle.circle(80)
    turtle.left(360/number)
turtle.done

