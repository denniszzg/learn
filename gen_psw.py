#在26个大小写字母和数字组成的列表中生成一个8位密码

from random import randint
def psw():
    mi = ''
    for i in range(8):
        u = randint(0,62)
        if u >= 10:     #大写65~90，小写97~122
            if u > 35:
                mi += chr(u+61)
            else:
                mi += chr(u+55)
            
        else:
            mi += str(u)
    return mi
print("随机密码为：%s"%psw())

    
