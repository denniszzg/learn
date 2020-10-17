#7digit.py
#coding:utf-8
import turtle as t
import time
t.hideturtle()
def drawGap():# 定义间隔
    t.penup()
    t.fd(3)
def drawLine(draw): #定义画线
    drawGap()
    t.pendown() if draw else t.penup()
    t.fd(15)
    drawGap()
    t.right(90)
def drawDigit(digit):   #定义画7段数码管
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    t.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    t.right(180)
    t.penup()
    t.fd(15)
def drawDate(date):
    t.pencolor('red')
    for i in date:
        if i == '-':
            t.write('年', font=('Arial', 18, "normal"))
            t.pencolor('green')
            t.fd(20)
        elif i == '+':
            t.write('月', font=('Arial', 18, "normal"))
            t.pencolor('blue')
            t.fd(20)
        elif i == '=':
            t.write('日', font=('Arial', 18, "normal"))
            t.fd(40)
        elif i == ':':
            t.write(':', font=('Arial', 18, "normal"))
            t.fd(10)
        else:
            drawDigit(eval(i))
def main():
    t.setup(640,480)
    t.pencolor("red")
    t.pensize(5)
    t.penup()
    t.bk(300)
    drawDate(time.strftime("%Y-%m+%d=%H:%M", time.gmtime()))
    
    t.done()
main()