import sys
input = sys.stdin.readline

n, m = map(int, input().split())
castle = [list(input().rstrip()) for _ in range(n)]

num_r, num_c = [0 for _ in range(n)], [0 for _ in range(m)]
for i in range(n):
  for j in range(m):
    if castle[i][j] == 'X':
      num_r[i] += 1
      num_c[j] += 1

res = max(num_r.count(0), num_c.count(0))
print(res)