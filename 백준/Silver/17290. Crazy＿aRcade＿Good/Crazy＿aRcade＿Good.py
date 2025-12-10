import sys
input = sys.stdin.readline

r, c = map(int, input().split())

result = [[True for _ in range(10)] for _ in range(10)]
for i in range(10):
  arr = list(input().rstrip())

  for j in range(10):
    if arr[j] == 'o':
      for k in range(10):
        result[i][k] = False
        result[k][j] = False

distance = 10**9
for a in range(10):
  for b in range(10):
    if result[a][b] == True:
      dist = abs((a+1)-r) + abs((b+1)-c)
      if dist < distance:
        distance = dist

print(distance)