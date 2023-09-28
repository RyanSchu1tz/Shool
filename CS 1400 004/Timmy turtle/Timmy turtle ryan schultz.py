'''
Ryan Schultz

def: square(hight, width, color): (100, 100, red)
def: triangle(sides, color):      (100, blue)
def: circle(size, color):         (15, green)
'''
import turtle

t = turtle.Turtle()

def square(hight, width, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range (2):
        t.forward(width)
        t.lt(90)
        t.forward(hight)
        t.lt(90)
    t.end_fill()

def triangle(sides, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range (3):
        t.forward(sides)
        t.lt(120)
    t.end_fill()

def circle(size, color):  
    t.fillcolor(color)
    t.begin_fill()
    for i in range (90):
        t.forward(size)
        t.lt(4)
    t.end_fill()
'''
t.penup()
t.forward()
t.lt()
t.forward()
t.pendown()
'''
STriangles = 7
t.penup()
t.backward(490)
t.pendown()
while STriangles >= 0:
    triangle(70, 'dark violet')
    t.forward(70)
    STriangles -= 1

t.lt(90)
for i in range(3):
    circle(3,'chartreuse')
    t.penup()
    t.forward(90)
    t.pendown()
t.penup()
t.backward(270)
t.pendown()
iff = 3
ifff = 0
if iff > ifff:
    t.lt(30)
    square(30, 31, 'medium spring green')
    t.rt(30)
    
t.speed('fast')
square(100,100, 'red')

t.penup()
t.forward(100)
t.lt(57)
t.forward(276)
t.pendown()
triangle(120, 'green')

t.penup()                       
t.forward(100)
t.rt(134)
t.forward(178)
t.pendown()
circle(1,'blue')

t.penup()
t.forward(230)
t.rt(111)
t.forward(400)
t.pendown()
circle(17, 'pink')

t.penup()
t.forward(200)
t.lt(23)
t.forward(23)
t.pendown()
triangle(170, 'lime')

t.penup()
t.forward(7)
t.lt(7)
t.forward(7)
t.pendown()
square(7, 200, 'cyan')

t.penup()
t.forward(89)
t.rt(89)
t.forward(89)
t.pendown()
triangle(89, 'dark magenta')

''' #Manual control
while True:
    direction = input()
    if direction == 'w':
        t.penup()
        t.forward(50)
        t.pendown()
    if direction == 'a':
        t.penup()
        t.lt(90)
        t.pendown()
    if direction == 'd':
        t.penup()
        t.rt(90)
        t.pendown()
    if direction == 's':
        t.penup()
        t.backward(50)
        t.pendown()
    if direction == '1':
        t.pendown()
        square(100,100, 'red')
        t.penup()
    if direction == '2':
        t.pendown()
        triangle(120, 'green')
        t.penup()
    if direction == '3':
        t.pendown()
        t.speed(0)
        circle(3,'blue')
        t.speed(1)
        t.penup()
'''



turtle.mainloop()