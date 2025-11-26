import sys
input = sys.stdin.readline

s, n, m = map(int, input().split())
comp = 0
for _ in range(n+m):
  o = int(input())

  if o == 1:
    comp += 1
    if comp > s:
      s *= 2
  else:
    comp -= 1

print(s)