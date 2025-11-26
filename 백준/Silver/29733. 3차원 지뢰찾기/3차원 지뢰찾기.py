import sys
input = sys.stdin.readline

r, c, h = map(int, input().split())

cube = [[list(input().rstrip()) for _ in range(r)] for _ in range(h)]
result = [[[None] * c for _ in range(r)] for _ in range(h)]

for i in range(h):
  for j in range(r):
    for k in range(c):
      if cube[i][j][k] == '*':
        result[i][j][k] = '*'

      elif cube[i][j][k] == '.':
        cnt = 0
        for i_ in range(max(i-1, 0), min(i+2, h)):
          for j_ in range(max(j-1, 0), min(j+2, r)):
            for k_ in range(max(k-1, 0), min(k+2, c)):
              if cube[i_][j_][k_] == '*':
                cnt += 1
        
        result[i][j][k] = cnt % 10

for a in result:
  for b in a:
    print(*b, sep='')