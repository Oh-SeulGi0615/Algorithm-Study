import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    a = int(input())
    arr.append(a)

if len(arr) == 1:
    print(0)
else:
    arr_ = arr[1:]
    me = arr[0]

    cnt = 0
    while True:
        if me > max(arr_):
            break
        me += 1
        arr_[arr_.index(max(arr_))] -= 1
        cnt += 1

    print(cnt)