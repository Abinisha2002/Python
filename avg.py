# import turtle
# def draw_circle(pen):
#     # outer circle
#     pen.setposition(0, -280)
#     pen.pendown()
#     pen.begin_fill()
#     pen.color('blue')
#     pen.pencolor('white')
#     pen.circle(300)
#     pen.end_fill()
#     pen.penup()


# def draw_circle2(pen):
#     # inner circle
#     pen.pensize(2)
#     pen.setposition(0, -230)
#     pen.pendown()
#     pen.begin_fill()
#     pen.color('black')
#     pen.circle(250)
#     pen.end_fill()
#     pen.penup()


# def draw_A(pen):
#     # drawing ‘A’
#     pen.setposition(30, -110)
#     pen.pendown()
#     pen.begin_fill()
#     pen.color('red')
#     pen.pensize(10)
#     pen.pencolor('white')
#     pen.forward(23)
#     pen.backward(123)
#     pen.left(60)
#     pen.backward(220)
#     pen.right(60)
#     pen.backward(100)
#     pen.right(117)
#     pen.backward(710)
#     pen.right(63)
#     pen.backward(110)
#     pen.right(90)
#     pen.backward(510)
#     pen.right(90)
#     pen.backward(100)
#     pen.right(90)
#     pen.backward(70)
#     pen.end_fill()
#     pen.penup()


# def draw_triangle(pen):
#     # Triangle shape in ‘A’ to make it look like 2d
#     pen.pensize(10)
#     pen.setposition(53, -40)
#     pen.pendown()
#     pen.begin_fill()
#     pen.color('black')
#     pen.pencolor('white')
#     pen.right(90)
#     pen.forward(100)
#     pen.right(115)
#     pen.forward(250)
#     pen.right(157)
#     pen.forward(227)
#     pen.end_fill()


# def draw_arrow(pen):
#     # arrow
#     pen.backward(80)
#     pen.left(42)
#     pen.forward(147)
#     pen.right(83)
#     pen.forward(140)


# if __name__ == '__main__':
#     win = turtle.Screen()
#     win.bgcolor('black')

#     avengers = turtle.Turtle()
#     avengers.speed(1)
#     avengers.pensize(10)
#     avengers.penup()

#     draw_circle(avengers)
#     draw_circle2(avengers)
#     draw_A(avengers)
#     draw_triangle(avengers)
#     draw_arrow(avengers)
#     avengers.penup()

#     avengers.setposition(300,300)
#     avengers.pencolor("red")

#     avengers.write("Code by Mahesh")
#     avengers.hideturtle()
#     turtle.done()




# import turtle
# s=turtle.Turtle()
# s.color("red")
# s.begin_fill()
# s.circle(150)
# s.end_fill()
# s.speed(0)

# s.penup()
# s.setpos(70,180)
# s.pendown()
# s.color("black")
# s.begin_fill()
# s.speed(0)
# s.right(90)
# s.forward(10)
# for x in range(145):
#     s.right(1)
#     s.forward(0.25)
# s.right(30)
# s.forward(20)
# for x in range(145):
#     s.right(1)
#     s.forward(0.25)
# s.end_fill()

# s.penup()
# s.setpos(-30,180)
# s.pendown()
# s.color("black")
# s.begin_fill()
# s.right(45)
# s.forward(10)
# for x in range(145):
#     s.right(1)
#     s.forward(0.25)
# s.right(30)
# s.forward(20)
# for x in range(145):
#     s.right(1)
#     s.forward(0.25)
# s.end_fill()

# s.penup()
# s.setpos(-19,190)
# s.pendown()
# s.pensize(10)
# s.color("black")
# s.right(170)
# s.forward(10)
# for x in range(50):
#     s.left(1)
#     s.forward(1)
# s.penup()
# s.setpos(30,190)
# s.pendown()
# s.pensize(10)
# s.color("black")
# s.right(150)
# s.forward(10)
# for x in range(50):
#     s.right(1)
#     s.forward(1)

# s.penup()
# s.setpos(-30,73)
# s.pendown()
# s.left(45)
# for x in range(70):
#     s.right(1)
#     s.forward(1)








# turtle.done()