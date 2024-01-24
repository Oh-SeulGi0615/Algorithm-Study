import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
palace = [[0] * n for _ in range(m)]

direction = deque([(1, 0), (0, 1), (-1, 0), (0, -1)])
now_x, now_y = 0, 0

cnt = n * m
while True:
    cnt -= 1
    if cnt <= 0:
        break
    
    if now_x+direction[0][0] < 0 or now_y+direction[0][1] < 0 or now_x+direction[0][0] >= n or now_y+direction[0][1] >= m or palace[now_y+direction[0][1]][now_x+direction[0][0]] == 1:
        direction.rotate(-1)
    
    if palace[now_y][now_x] == 0:
        palace[now_y][now_x] = 1
        now_x += direction[0][0]
        now_y += direction[0][1]

print(now_x, now_y)