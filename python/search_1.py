data = [57, 39, 10, 78, 60, 30, 55, 92, 50]
n = len(data)

key = 50
flg = False

for i in range(n):
    if data[i] == key:
        print("data[{}]が{}です".format(i, key))
        flg = True
        break

if flg == False:
    print(str(key)+"は存在しません")

