import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())

    arr = []
    for _ in range(b):
        x, y = map(int, input().split())
        arr.append(x*y)
    
    arr.sort()
    arr = arr[::-1]

    cnt = 0
    for i in range(b):
        if a > 0:
            a -= arr[i]
            cnt += 1

    print(cnt)