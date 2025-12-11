import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [i for i in range(1, n+1)]

if n == k and k % 2 == 0:
  print('YES')
elif n == k and k % 2 == 1:
  print('NO')
elif n > k:
  print('YES')