import turtle
import math

screen = turtle.Screen()
screen.setup(900, 900)
screen.bgcolor("#0a192f")
screen.title("TECH CLUB LOGO")

t = turtle.Turtle()
t.speed(0)
t.pensize(3)
t.hideturtle()

# Draw Hexagon
t.color("#00ffff")
t.penup()
t.goto(0, 220)
t.pendown()

for i in range(6):
    angle = math.radians(60 * i)
    x = 220 * math.cos(angle)
    y = 220 * math.sin(angle)

    if i == 0:
        t.penup()
        t.goto(x, y)
        t.pendown()
    else:
        t.goto(x, y)

t.goto(220, 0)

# Circuit Lines
circuits = [
    (-150,100), (-120,-80), (140,90),
    (100,-120), (0,150), (0,-150)
]

for x,y in circuits:
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.goto(x,y)

    t.penup()
    t.goto(x,y)
    t.dot(15,"#00ffff")

# Brain Shape
t.color("#00ff99")
t.penup()
t.goto(-60,50)
t.pendown()

t.circle(40,180)
t.circle(20,180)

t.penup()
t.goto(60,50)
t.pendown()

t.circle(-40,180)
t.circle(-20,180)

# Coding Symbol
t.color("white")

t.penup()
t.goto(-90,-20)
t.pendown()
t.write("<", font=("Arial",50,"bold"))

t.penup()
t.goto(20,-20)
t.pendown()
t.write(">", font=("Arial",50,"bold"))

t.penup()
t.goto(-10,20)
t.pendown()
t.goto(-35,-40)

# Binary Ring
binary = "10101001100101011010"

radius = 170

for i, char in enumerate(binary):
    angle = (360/len(binary))*i

    x = radius * math.cos(math.radians(angle))
    y = radius * math.sin(math.radians(angle))

    t.penup()
    t.goto(x,y)

    t.color("#64ffda")
    t.write(char,font=("Arial",12,"bold"))

# Club Name
t.penup()
t.goto(-120,-280)
t.color("white")
t.write("TECH CLUB",
        font=("Arial",32,"bold"))

# Motto
t.penup()
t.goto(-140,-320)
t.color("#64ffda")
t.write("Innovate • Code • Create",
        font=("Arial",16,"normal"))

screen.mainloop()
