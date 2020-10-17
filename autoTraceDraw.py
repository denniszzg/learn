import turtle as t
t.title("自动轨迹绘制")
t.setup(800, 600, 0, 0)
t.pensize(5)
t.pencolor("red")

#读取数据
data = []
f = open("data.txt")
for line in f:
    line = line.replace("\n","")
    data.append(list(map(eval, line.split(",") ) ) )
f.close()

#自动绘制
for i in range(len(data)):
    t.pencolor(data[i][3],data[i][4],data[i][5])
    t.fd(data[i][1])
    if data[i][1]:
        t.rt(data[i][2])
    else:
        t.lt(data[i][2])
     
