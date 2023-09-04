import sys
input = sys.stdin.readline

c = int(input())
cnt = 1
while True:
    if c == 1:
        break
    if c % 2 == 0:
        c /= 2
        cnt += 1
    else:
        c = 3*c + 1
        cnt += 1

print(cnt)