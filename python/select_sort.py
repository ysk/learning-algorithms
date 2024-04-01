# coding: utf-8

data = [9, 3, 7, 1, 4, 2, 5, 8, 6, 0]
n  = int(len(data))

for i in range(0, n-1):
    for j in range(n-1, i, -1):
        if data[j] < data[m]:
            m = j
        data[i], data[m] = data[m], data[i]
        print(data, i+1)

print(data, "ソート後のデータ")