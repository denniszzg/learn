#coding: utf-8
import wordcloud as wc
import jieba
#import matplotlib.pyplot as plt
from scipy.misc import imread

bg_pic = imread("china.jpg")
txt = open("report.txt", 'r', encoding='utf-8').read()
ls = jieba.lcut(txt)
words = " ".join(ls)
c = wc.WordCloud(mask=bg_pic,background_color='white',font_path = 'simsun.ttc')
c.generate(words)
c.to_file("c.png")
