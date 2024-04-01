# coding: utf-8

data = [9, 3, 7, 1, 4, 2, 5, 8, 6, 0]
n  = int(len(data))
print(data, "ソート前のデータ")
for i in range(0,n-1):
    for j in range(n-1, i, -1):
        if data[j-1] > data[j]:
            data[j], data[j-1] = data[j-1], data[j]

print(data, "ソート後のデータ")