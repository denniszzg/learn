#Textbar.py

'''
https://python123.io/student/courses/371/groups/1920/intro
"Python 语言程序设计"(中国大学 MOOC 平台) 
练习3: 基本数据类型 (第3周)

'''

import time
scale = 657
print("{:-^75}\n" .format("执行开始"))
#print("执行开始".center(scale//2,"-"))  #"//"取回商的整数部分，向下取整。-9//2，结果为-5
start = time.perf_counter()
for i in range(scale+1):
    a = (i/scale)*100
    b = "=" * i
    c = " " * (scale - i)
    dur = time.perf_counter() - start
    print("\r{:<3.0f}%[{}=>{}]{:.2f}s".format(a,b,c,dur), end="")
    time.sleep(0.1)
#print("\n"+"执行结束".center(scale//2,"-"))
print("\n\n{:-^75}" .format("执行结束"))