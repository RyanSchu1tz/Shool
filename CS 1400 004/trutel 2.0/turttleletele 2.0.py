'''
By: Ryan Schultz
Date: 10/22/2023
docstring
'''

import turtle

t = turtle.Turtle()



def stars():
    for i in range(6):
        t.up()
        t.goto(((-350)+125*i),350)
        t.down()
        octagon(3,2, 'green')
        t.up()
        t.goto(((-335)+100*i),400)
        t.down()
        dodecagon(2,2, 'purple')
        t.goto(((-315)+125*i),325)
        t.up()
        t.goto(((-300)+100*i),350)
        t.down()
        octagon(2,2, 'green')
        t.up()
        t.goto(((-275)+125*i),375)
        t.down()
        dodecagon(1,2, 'purple')
        t.goto(((-265)+100*i),300)

def mountain():
    t.up()
    t.goto(-500,0)
    t.down()
    triangle(150,2, 'gray')
    t.forward(100)
    triangle(125,2, 'gray')
    t.forward(100)
    triangle(200,2, 'gray')
    t.forward(200)
    triangle(150,2, 'gray')
    t.forward(100)
    triangle(125,2, 'gray')
    t.forward(100)
    triangle(200,2, 'gray')

def ground():
    t.up()
    t.goto(-500,-500)
    t.down()
    rectangle(250,500,2, 'saddle brown')

def sun():
    t.up()
    t.goto(-400,300)
    t.down()
    circle(5, 2,'yellow')
  
def window():
    t.down()
    rectangle(65,15,2, 'white')
    t.up()
    t.forward(15)
    t.down()
    t.left(90)
    t.forward(130)
    t.left(90)
    t.forward(15)
    t.left(90)
    t.forward(65)
    t.left(90)
    t.forward(30)

def house():
    t.up()
    t.goto(-130,-140)
    t.down()
    square(150,"purple")
    t.forward(50)
    rectangle(50,25,2, 'red')
    t.up()
    t.backward(40)
    t.left(90)
    t.forward(10)
    t.right(90)
    window()
    t.up()
    t.right(90)
    t.forward(65)
    t.left(90)
    t.forward(70)
    window()
    t.up()
    t.backward(140)
    t.left(90)
    t.forward(75)
    t.right(90)
    t.down()
    triangle(75,2, 'slate blue')
    
def background():
    t.up()
    t.goto(-500,-500)
    t.down()
    color = input('input a color ("slate blue" is my suggestion): ')
    square(1000,color)
    t.up()
    t.goto(0,0)
    t.down()
   

def square(scale, color):
    '''base size 1,1 square'''
    t.fillcolor(color)
    t.begin_fill()
    for i in range (4):
        t.forward(1 * scale)
        t.lt(90)
    t.end_fill()

def rectangle(hight, width, scale, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range (2):
        t.forward(width * scale)
        t.lt(90)
        t.forward(hight * scale)
        t.lt(90)
    t.end_fill()

def triangle(sides,scale, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range (3):
        t.forward(sides * scale)
        t.lt(120)
    t.end_fill()
    
def circle(size,scale, color):  
    t.fillcolor(color)
    t.begin_fill()
    for i in range (90):
        t.forward(size * scale)
        t.lt(4)
    t.end_fill()



def octagon(sides,scale, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range (8):
        t.forward(sides * scale)
        t.lt(45)
    t.end_fill()

def dodecagon(sides,scale, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range (12):
        t.forward(sides * scale)
        t.lt(30)
    t.end_fill()
    t.up()

def main():
    background()
    stars()
    sun()
    mountain()
    ground()
    house()
    turtle.done()
# program kicks off here -- must call turtle.done() AFTER main().
if __name__ == "__main__":
    main()
    
    
    '''
    triangle(10,2, 'gray')
    square(150,"red")
    rectangle(100,50,2, 'red')
    circle(1, 2,'blue')
    octagon(17,2, 'green')
    dodecagon(15,2, 'purple')
    '''



