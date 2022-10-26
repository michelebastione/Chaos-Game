import random
import turtle

def Sierpinski_Triangle():
    x, y = 0, 20
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.dot()
    turtle.tracer(0, 0)
    
    for i in range(10**4):
        z=random.randint(0,2)
        if i%10**2 == 0:
            turtle.update()
            turtle.tracer(0, 0)
        if z==0:
            turtle.penup()
            a=turtle.towards(-200,-200)
            turtle.setheading(a)
            b=turtle.distance(-200,-200)/2
            turtle.forward(b)
            turtle.pendown()
            turtle.dot()
        elif z==1:
            turtle.penup()
            a=turtle.towards(200,-200)
            turtle.setheading(a)
            b=turtle.distance(200,-200)/2
            turtle.forward(b)
            turtle.pendown()
            turtle.dot()
        else:
            turtle.penup()
            a=turtle.towards(0,227.2136)
            turtle.setheading(a)
            b=turtle.distance(0,227.2136)/2
            turtle.forward(b)
            turtle.pendown()
            turtle.dot()

if __name__ == "__main__":
    Sierpinski_Triangle()
