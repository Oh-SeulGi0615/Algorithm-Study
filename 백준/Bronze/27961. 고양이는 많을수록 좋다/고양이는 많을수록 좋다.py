import sys
input = sys.stdin.readline

n = int(input())

cnt = 0
while n > 0:
    if n == 1:
        n -= 1
        cnt += 1
        break

    if n % 2 == 0:
        n = int(n / 2)
        cnt += 1
    else:
        n  = int(n / 2) +1
        cnt += 1

print(cnt)