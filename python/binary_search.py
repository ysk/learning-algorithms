data = [1,2,3,5,6,7,8,20,25,48,50,57,72,89,92,100]

n = len(data)

key = int(input('探す値を入力してください'))
left = 0
right = len(data) - 1
flag = False

while left <= right:
    mid = (left+right) // 2
    print("L={} M={} R={}".format(left, mid, right))

    if data[mid] == key:
        print("data[{}]が{}です".format(mid, key))
        flag = True
        break
    if data[mid] < key:
        left = mid+1
    else:
        right = mid-1

if flag == False:
    print("その値は見つかりませんでした")

