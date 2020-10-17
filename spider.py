
from lxml import etree


obj= etree.HTML(https://python123.io/student/courses/371/materials)
list = obj.xpath('//*[@id="app"]/div/div[1]/div[1]/div[1]/section/div/div[2]/div[2]/div[2]/div/div/div[2]/div/p[52]/a/text()')
print(list)

