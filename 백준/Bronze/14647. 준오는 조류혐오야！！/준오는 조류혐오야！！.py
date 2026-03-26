import sys
input = sys.stdin.readline

n, m = map(int, input().split())

bingo = []
for _ in range(n):
  arr = list(input().split())
  bingo.append(arr)

best, loc_h, loc_v = -1, -1, -1
for i in range(n):
  cnt = 0
  for j in range(m):
    cnt += bingo[i][j].count('9')
  if cnt > best:
    best = cnt
    loc_h = i
    loc_v = -1

for i in range(m):
  cnt = 0
  for j in range(n):
    cnt += bingo[j][i].count('9')
  if cnt > best:
    best = cnt
    loc_v = i
    loc_h = -1

if loc_h >= 0:
  bingo[loc_h] = ['0'] * m
elif loc_v >= 0:
  for k in range(n):
    bingo[k][loc_v] = '0'

res = 0
for a in range(n):
  for b in range(m):
    res += bingo[a][b].count('9')

print(res)