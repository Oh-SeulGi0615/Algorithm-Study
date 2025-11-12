import sys

n = int(sys.stdin.readline())

sum = 1
for i in range(n, 1, -1):
  sum += i

print(sum)