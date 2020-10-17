#kochDraw.py

import turtle as t
def koch(size, n):  #size是长度，n是阶数
    if n == 0:
        t.fd(size)
    else:
        for angle in [0,60,-120,60]:
            t.left(angle)
            koch(size/3, n-1)
def main():
    t.setup(800, 400)
    t.pu()
    t.goto(-200, 100)
    t.pd()
    t.pensize(2)
    level = 2
    for i in range(3):
        koch(200,level)
        t.right(360/3)
    t.hideturtle()
    t.done()
main()

