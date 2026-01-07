import sys
input = sys.stdin.readline

n = int(input())
min_y, max_y = 10**9, -10**9

for _ in range(n):
  x, y = map(int, input().split())

  if y < min_y:
    min_y = y
  if y > max_y:
    max_y = y

print(abs(max_y - min_y))