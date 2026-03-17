import sys
input = sys.stdin.readline

h, m = map(int, input().split(':'))
pannel = list(map(int, input().split()))

def check_loc(h, m):
  res = ((h % 12) * 60) + m
  return (res // 120) + 1

l = int(input())
for _ in range(l):
  a = list(input().split())
  s, ms = map(int, a[0].split('.'))
  c = a[1]

  time = 1000 * s + ms
  if time >= 60000:
    break

  if c == '^':
    loc = check_loc(h, m)
    pannel[loc-1] = 0
  elif c == '10MIN':
    a, b = divmod((m + 10), 60)
    m = b
    h += a
  elif c == '30MIN':
    a, b = divmod((m + 30), 60)
    m = b
    h += a
  elif c == '50MIN':
    a, b = divmod((m + 50), 60)
    m = b
    h += a
  elif c == '2HOUR':
    h += 2
  elif c == '4HOUR':
    h += 4
  elif c == '9HOUR':
    h += 9

print(min(sum(pannel), 100))