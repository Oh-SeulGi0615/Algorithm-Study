import sys

arr = []
dict_ = {}
cnt = 1
idx = 1
while True:
    for i in range(cnt, 0, -1):
        arr.append([cnt+1-i, i])
        dict_[(cnt+1-i, i)] = idx
        idx += 1

    cnt += 1
    if cnt == 300:
        break

n = int(sys.stdin.readline())
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    x_ = arr[x-1][0] + arr[y-1][0]
    y_ = arr[x-1][1] + arr[y-1][1]

    print(dict_[(x_, y_)])