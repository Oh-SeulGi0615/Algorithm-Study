import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

h = arr[0]
cnt = 0
best = 0
for i in range(1,n):
    if arr[i] >= h:
        h = arr[i]
        cnt = 0
    else:
        cnt += 1
    best = max(best, cnt)

print(best)