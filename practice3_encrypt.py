#encrypt.py

'''

https://python123.io/student/courses/371/groups/1920/intro
"Python 语言程序设计"(中国大学 MOOC 平台) 
练习3: 基本数据类型 (第3周)

'''



'''
方法1
'''
# str = input()
# strLen = len(str)
   
# for i in range(strLen):
    # if ord(str[i]) in range(97, 123):  #lower
        # c = (ord(str[i]) - 97 + 3) % 26
        # print(chr(97 + c), end="")
    # elif ord(str[i]) in range(65, 100): #upper
        # c = (ord(str[i]) - 65 + 3) % 26
        # print(chr(65 + c), end="")
    # else: #others
        # print(str[i], end="")
        
'''
方法2
'''

str = input()
temp = ""
for s in str:
    if 'a' <= s <= 'z':
        temp += chr( ord('a') + ( ord(s) - ord('a') + 3 )%26 )
    elif 'A' <= s <= 'Z':
        temp += chr( ord('A') + ( ord(s) - ord('A') + 3 )%26 )
    else:
        temp += s
print(temp)
