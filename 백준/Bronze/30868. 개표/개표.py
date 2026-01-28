import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n = int(input())

  a, b = divmod(n, 5)
  res = ''
  res += '++++ ' * a + '|' * b

  print(res)