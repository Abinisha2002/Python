import turtle
def circle(a):
    a.setposition(0, -280)
    a.pendown()
    a.begin_fill()
    a.color('blue')
    a.pencolor('black')
    a.circle(300)
    a.end_fill()
    a.penup()

def circle2(a):
    a.setpos(2,-200)
    a.pendown()
    a.pensize(2)
    a.begin_fill()
    a.color("black")
    a.pencolor("white")
    a.circle(200)
    a.end_fill()
    a.penup()


def lettern(a):
    a.penup()
    a.setpos(-70,100)
    a.pensize(8)
    a.pendown()
    a.left(150)
    a.forward(150)
    a.left(120)
    a.forward(350)
    a.left(120)
    a.forward(100)
    a.left(63)
    a.forward(170)
    a.right(120)
    a.forward(230)
    a.left(120)
    a.forward(330)
    a.right(50)
    a.forward(80)
    a.right(130)
    a.forward(500)
    a.right(120)
    a.forward(160)
    
   
  

win = turtle.Screen()
win.bgcolor('blue')

avg= turtle.Turtle()
avg.speed(10)
avg.pensize(10)
avg.penup() 


circle(avg)
circle2(avg)
lettern(avg) 
avg.penup()


avg.setpos(300,300)
avg.color("white")
avg.write("design by abis")  
turtle.done()
