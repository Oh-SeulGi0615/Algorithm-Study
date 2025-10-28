import sys

n = int(sys.stdin.readline())

arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
graph = [[0] * n for _ in range(n)]

for i in range(n):
  for j in range(i, n):
    if arr[i][j] == 'Y' and arr[j][i] == 'Y':
      graph[i][j] = 2
      graph[j][i] = 2

for i in range(n):
  for j in range(n):
    for k in range(n):
      if arr[i][j] == 'Y' and arr[j][k] == 'Y' and arr[i][k] == 'N':
        if i != k:
          graph[i][k] = 2
          graph[k][i] = 2

result = 0
for i in graph:
  if i.count(2) > result:
    result = i.count(2)
print(result)