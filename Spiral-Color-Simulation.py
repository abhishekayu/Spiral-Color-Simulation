import turtle 
"Abhishek Patel @imdarkcoder"
colors = ["orange", "red" , "pink" , "yellow" , "blue" , "green" ]

screen = turtle.Screen()

t=turtle.Turtle()
t.speed(0)

screen.bgcolor("black")

for x in range (360):
    t.pencolor(colors[x%6])
    t.width(x / 5 + 1)
    t.forward(x)
    t.left(20)

