import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]

arr_c = [i for i in range(1, c+1)]
for j in arr:
    for k in range(1, (c // j) + 1):
        arr_c[k*j - 1] = -1

print(arr_c.count(-1))