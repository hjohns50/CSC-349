from sort_compare import *
import random
import matplotlib.pyplot as plt

num_ele = 5000
#x = [10, 4, 9, 2, 4]
#y = [10, 8, 2, 4, 9]

x = [0] * 500
y = [0] * 500
index = 0
for index in range(500):
    #print(index)
    random.seed(1234)
    rand1 = [0] * num_ele
    rand2 = [0] * num_ele
    rand3 = [0] * num_ele
    i = 0
    randoms = random.sample(range(65535), num_ele)
    #print(len(randoms))
    time1 = float(merge_sort(randoms))
    x[index] = num_ele
    y[index] = time1
    #print(x[index], y[index])
    num_ele += 10
plt.scatter(x, y)
plt.show()
