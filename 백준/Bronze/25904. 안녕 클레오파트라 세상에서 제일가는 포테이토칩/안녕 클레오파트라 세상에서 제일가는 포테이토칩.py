import sys
input = sys.stdin.readline

n, x = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
while True:
    if arr[cnt] < x:
        print(cnt+1)
        break
    x += 1
    cnt += 1
    if cnt == n:
        cnt = 0