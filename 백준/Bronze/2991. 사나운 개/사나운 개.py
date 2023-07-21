import sys
input = sys.stdin.readline

a, b, c, d = map(int, input().split())
arr = list(map(int, input().split()))

for i in arr:
    x1, y1 = divmod(i, (a+b))
    x2, y2 = divmod(i, (c+d))

    cnt = 0
    if 0 < y1 <= a:
        cnt += 1
    if 0 < y2 <= c:
        cnt += 1
    
    print(cnt)