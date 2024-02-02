import sys
input = sys.stdin.readline

n = int(input())

dots = 1
for i in range(1, n+1):
    dots += ((i-1) * 3) + 4

print(dots % 45678)