import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, d = map(int, input().split())

    cnt = 0
    for _ in range(n):
        v, f, c = map(int, input().split())

        time = f / c
        distance = v * time

        if distance >= d:
            cnt += 1

    print(cnt)