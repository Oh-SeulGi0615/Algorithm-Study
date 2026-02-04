import sys
input = sys.stdin.readline

n = int(input())
i_set = set()
cnt = 0

for _ in range(n):
  p, i = map(int, input().split())

  if i == 1:
    if p not in i_set:
      i_set.add(p)
    else:
      cnt += 1
  elif i == 0:
    if p in i_set:
      i_set.remove(p)
    else:
      cnt += 1
cnt += len(i_set)
print(cnt)