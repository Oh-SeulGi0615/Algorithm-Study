import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

if k != 0:
  arr.sort()

for _ in range(k):
  l, r, a = map(int, input().split())
  arr[l-1:r] = map(lambda x: x+a, arr[l-1:r])
  arr = sorted(arr)

print(*arr)