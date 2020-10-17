import random       #导入random随机数模块
num1 = random.randint(1,10)  #电脑在1到10之间取一个随机数，赋值给变量num1
num2 = random.randint(1,10)  #电脑在1到10之间取一个随机数，赋值给变量num2
print("-------------10以内加法----------------")    #显示字符串内容
print(num1, end='')
print ("+", end='')
print(num2, end='')
print("= ？")

#显示随机数1 + 随机数2 = ？
temp = input('答案：') #显示字符串内容，并让用户输入
answer = int(temp)  #设用户输入值为整型并赋值给变量answer

#下面为循环语句，循环内容为while下面的缩进内容，当用户输入值不等于num1+num2时运行
while answer != num1 + num2:    
    temp = input('答错咯，再试一次吧：')  #用户重新输入答案
    answer = int(temp)    #将用户新的答案赋值给变量answer，并重新运行while循环体
print("❤❤❤❤❤媛媛你答对了，你好棒！！❤❤❤❤❤")
print("游戏结束")
print("-------------game over-----------------")
