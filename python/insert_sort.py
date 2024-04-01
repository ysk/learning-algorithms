# coding: utf-8

data = [9, 3, 7, 1, 4, 2, 5, 8, 6, 0]
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