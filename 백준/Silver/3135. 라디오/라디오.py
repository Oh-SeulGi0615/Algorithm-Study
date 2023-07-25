import sys
input = sys.stdin.readline

a, b = map(int, input().split())
arr = [int(input()) for i in range(int(input()))]

cnt1 = abs(a-b)

if b in arr:
    print(1)
else:
    cnt2 = 1
    c = abs(arr[0] - b)
    for i in range(1, len(arr)):
        if abs(arr[i] - b) < c:
            c = abs(arr[i] - b)

    cnt2 += c
    print(min(cnt1, cnt2))