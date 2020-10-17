#calBMI.py


try:
    weight, height = eval(input("请分别输入体重kg和身高m，以逗号隔开：") )
    bmi = weight / pow(height, 2)
    china, foreign = "", ""
    if bmi < 18.5:
        china, foreign = "偏瘦", "偏瘦"
    elif 18.5 <= bmi <= 24:
        china, foreign = "正常", "正常"
    elif 24 < bmi <= 25:
        china, foreign = "偏胖", "正常"
    elif 25 < bmi <= 28:
        china, foreign = "偏胖", "偏胖"
    elif 28 <= bmi <= 30:
        china, foreign = "肥胖", "偏胖"
    else:
        china, foreign = "肥胖", "肥胖"
    print("您的bmi指数为：{:.2f},按国内标准{}，按国际标准{}".format(bmi, china, foreign) )
except:
    print("请确认您的输入是否正确")