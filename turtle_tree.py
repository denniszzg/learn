from turtle import *
import time

#initialize
colormode(255)
speed(0)

lt(90)

lv = 14
l = 120
s = 45

width(lv)


r = 0
g = 0
b = 0
pencolor(r, g, b)

penup()
bk(l)
pendown()
fd(l)

def draw_tree(l, level):
    global r, g, b
    # save the current pen width
    w = width()

    # narrow the pen width
    width(w * 3.0 / 4.0)
    # set color:
    r = r + 1
    g = g + 2
    b = b + 3
    pencolor(r % 200, g % 200, b % 200)

    l = 3.0 / 4.0 * l

    lt(s)
    fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    rt(2 * s)
    fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    lt(s)

    # restore the previous pen width
    width(w)

speed("fastest")

draw_tree(l, 4)

#2019
hideturtle()
def drawGap():# 定义间隔
    penup()
    fd(3)
def drawLine(draw): #定义画线
    drawGap()
    pendown() if draw else penup()
    fd(15)
    drawGap()
    right(90)
def drawDigit(digit):   #定义画7段数码管
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    right(180)
    penup()
    fd(15)
def drawDate(date):
    global r, g, b
    
    for i in date:
        r = r + 111
        g = g + 333
        b = b + 555
        pencolor(r % 200, g % 200, b % 200)
        drawDigit(eval(i))
def main():
    setup(640,480)
    pencolor("red")
    pensize(5)
    penup()
    goto(-70,-180)
    seth(0)
    drawDate('2019')
    goto(240,-200)
    pencolor(25,25,25)
    write('T', font=('Arial', 8, "normal"))
    pencolor(125,25,125)
    fd(20)
    write('O', font=('Arial', 8, "normal"))
    pencolor(225,25,225)
    fd(20)
    write('M', font=('Arial', 8, "normal"))
    
    #write("via Tom")
    done()
main()

done()