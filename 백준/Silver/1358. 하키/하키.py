import sys
input = sys.stdin.readline

import math

w, h, x, y, p = map(int, input().split())

cnt = 0
for _ in range(p):
    x1, y1 = map(int, input().split())
    dist1 = math.sqrt((x - x1)**2 + ((y+(h/2)) - y1)**2)
    dist2 = math.sqrt(((x+w) - x1)**2 + ((y+(h/2)) - y1)**2)

    if x <= x1 <= (x + w) and y <= y1 <= (y + h):
        cnt += 1
    elif min(dist1, dist2) <= (h / 2):
        cnt += 1

print(cnt)