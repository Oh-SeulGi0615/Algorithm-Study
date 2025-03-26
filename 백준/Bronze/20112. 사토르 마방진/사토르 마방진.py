n = int(input())
l = []
for _ in range(n):
  arr = list(input())
  l.append(arr)

is_sator = 'YES'
for i in range(n):
  for j in range(n):
    if l[i][j] != l[j][i]:
      is_sator = 'NO'

print(is_sator)