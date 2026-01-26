import sys
input = sys.stdin.readline

n = int(input())
arr = sorted([int(input()) for _ in range(n)])

max_weight = arr[0] * n
for i in range(1, n):
  weight = arr[i] * (n-i)
  if weight > max_weight:
    max_weight = weight
print(max_weight)