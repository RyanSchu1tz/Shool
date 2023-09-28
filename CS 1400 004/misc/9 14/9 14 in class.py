import turtle

timmy = turtle.Turtle()

timmy.speed(3)

shape = input("input a number for how many sides you want 3,4, or 5 only: ") #3,4,5,

if shape == '3':
    print("green triangel")
    timmy.color("green")
    timmy.begin_fill()

    timmy.forward(100)
    timmy.left(120)
    timmy.forward(100)
    timmy.left(120)
    timmy.forward(100)
    timmy.left(120)

    timmy.end_fill()
elif shape == '4':
    print("blue square")
    timmy.color("blue")
    timmy.begin_fill()

    timmy.forward(100)
    timmy.left(90)
    timmy.forward(100)
    timmy.left(90)
    timmy.forward(100)
    timmy.left(90)
    timmy.forward(100)
    timmy.left(90)

    timmy.end_fill()

elif shape == '5':
    print("reb pentagon")
    timmy.color("red")
    timmy.begin_fill()

    timmy.forward(100)
    timmy.left(72)
    timmy.forward(100)
    timmy.left(72)
    timmy.forward(100)
    timmy.left(72)
    timmy.forward(100)
    timmy.left(72)
    timmy.forward(100)
    timmy.left(72)

    timmy.end_fill()
else:
    print("this is supposed to be an error messeage so uhh")
    print('"error message"')

turtle.done()