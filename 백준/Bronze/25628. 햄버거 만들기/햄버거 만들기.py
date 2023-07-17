import sys
input = sys.stdin.readline

x, y = map(int, input().split())

cnt = 0
while True:
    if x < 2 or y < 1:
        break
    x -= 2
    y -= 1
    cnt += 1

print(cnt)