import jieba
txt = open("2018baogao.txt", "r", encoding="utf-8").read()
#exclude = {}
words = jieba.lcut(txt)
counts ={}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1
items = list(counts.items() )
items.sort(key = lambda x:x[1], reverse = True)
for i in range(30):
    word, count = items[i]
    print("{:<10}{:>4}".format(word, count) )
