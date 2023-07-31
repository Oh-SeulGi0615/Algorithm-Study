import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    cnt = 0
    for i in arr:
        cnt += i // k

    print(cnt)