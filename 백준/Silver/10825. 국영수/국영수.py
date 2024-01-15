import sys
input = sys.stdin.readline

arr = [input().split() for _ in range(int(input()))]
for i in range(len(arr)):
    arr[i][1:] = list(map(int, arr[i][1:]))

arr = sorted(arr, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for j in arr:
    print(j[0])