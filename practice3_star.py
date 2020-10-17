#star.py

'''

https://python123.io/student/courses/371/groups/1920/intro
"Python 语言程序设计"(中国大学 MOOC 平台) 
练习3: 基本数据类型 (第3周)

'''

#方法一
'''
n = eval(input())
if n%2 == 1:
    for i in range(n):
        star = (2*i + 1) * "*"
        print(star.center(n, " "))
        if (2*i+1) == n:
            break
'''

#方法二
n = eval( input() )
for i in range(1,n+1,2):
    print( "{0:^{1}}".format("*"*i, n) )