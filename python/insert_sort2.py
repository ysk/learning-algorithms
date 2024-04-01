# coding: utf-8

import random
n = 50
data = [0]*n
for i in range(n):
    data[i] = random.randint(1, 50)

n  = int(len(data))
print(data, "ソート前のデータ")

for i in range(1,n):
    tmp = data[i]
    j = i
    while j>0 and data[j-1]>tmp:
        data[j] = data[j-1]
        j=j-1
    data[j]=tmp
    print(data, "ソート実行中")
    
print(data, "ソート後のデータ")