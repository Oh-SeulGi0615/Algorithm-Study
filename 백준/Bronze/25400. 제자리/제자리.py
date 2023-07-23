import sys
input = sys.stdin.readline

a = int(input())
arr = list(map(int, input().split()))

arr2 = []
cnt = 0
x = 1
while True:
    if arr == arr2:
        break
    if arr[x-1] != x:
        cnt += 1
        arr.pop(x-1)
    else:
        arr2.append(arr[x-1])
        x += 1

print(cnt)