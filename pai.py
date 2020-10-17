#paiCal.py
from random import random
pi = 0
n = 100000
x, y = 0, 0
count = 0
for i in range(n):
    x, y = random(), random()
    if pow((x**2 + y**2), 0.5) <= 1:
        count += 1
    else:
        pass
pi = 4 * count / n
print(pi)