import sys
input = sys.stdin.readline

a = int(input())

b = a
cnt = 0
x = 6
while x >= 0:
    c = 2 ** x
    d, e = divmod(b, c)
    if d > 0:
        cnt += 1
    b = e
    x -= 1

print(cnt)