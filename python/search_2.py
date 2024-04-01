data = [57, 39, 10, 78, 60, 30, 55, 92, 50]

n = len(data)
# print(n)
key = 57
i = 0

while i < n and data[i] != key:
    i += 1

if i == n:
    print(str(key)+"は存在しません")
else:
    print("data[{}]が{}です。".format(i, key))

