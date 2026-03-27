import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  r, c = map(int, input().split())

  if r == 1 and c == 1:
    print('dohoon')
  elif r == 1 or c == 1:
    print('jinseo')
    print(1, 1)
  elif r == c:
    print('dohoon')
  else:
    print('jinseo')
    print(min(r, c), min(r, c))