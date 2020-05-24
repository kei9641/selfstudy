import turtle as t
# t=turtle.Turtle()
t.shape("turtle")

def right():
    t.rt(90)
def left():
    t.lt(90)
def up():
    t.fd(100)
s = t.Screen()

s.onkey(right, "Right")
s.onkey(left, "Left")
s.onkey(up, "Up")
s.listen()

t.exitonclick()