#daydayup.py

'''

https://python123.io/student/courses/371/groups/1920/intro
"Python 语言程序设计"(中国大学 MOOC 平台) 
练习3: 基本数据类型 (第3周)

'''



def dayUP():
    dayup = 1
    for i in range(365):
        dayup *= 1 + 0.01
    return dayup
def workUP(dayfactor):
    workup = 1
    for i in range(365):
        if i%7 in [0,6]:
            workup *= 1 - 0.01
        else:
            workup *= 1 + dayfactor
    return workup
dayfactor = 0.01
while workUP(dayfactor) < dayUP():
    dayfactor += 0.001
print("工作日的努力参数是：%.3f"%dayfactor)