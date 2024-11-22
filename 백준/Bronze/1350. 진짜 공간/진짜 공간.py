n = int(input())
arr = list(map(int, input().split()))
cluster = int(input())

need_cluster = 0
for file in arr:
  a, b = divmod(file, cluster)
  if b > 0:
    need_cluster += (a + 1)
  else:
    need_cluster += a

print(need_cluster * cluster)