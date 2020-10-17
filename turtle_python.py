import turtle as t
t.setup(650,350,200,200)
t.penup()
t.fd(-250)
t.pendown()
t.pensize(40)
t.colormode(255)
r, g, b = 254, 215, 0
t.pencolor(r, g, b)
t.seth(-40)
t.hideturtle()
for i in range(4):
    t.circle(40,80)
    t.circle(-40,80)
    r -= 15
    g -= 35
    b += 35
    t.pencolor(r, g, b)
t.circle(40,80/2)
t.fd(40)
t.circle(16,180)
t.fd(40*2/3)
t.showturtle()
t.done()   


