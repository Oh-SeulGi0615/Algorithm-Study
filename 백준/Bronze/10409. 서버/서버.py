import sys
input = sys.stdin.readline

n, t = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
if sum(arr) < t:
    print(n)
else:
    for i in range(len(arr)):
        cnt += arr[i]
        if cnt > t:
            print(i)
            break