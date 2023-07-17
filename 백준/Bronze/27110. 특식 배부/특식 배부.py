import sys
input = sys.stdin.readline

n = int(input())
a, b, c = map(int, input().split())

sum = 0
if a > n:
    sum += n
else:
    sum += a

if b > n:
    sum += n
else:
    sum += b

if c > n:
    sum += n
else:
    sum += c

print(sum)