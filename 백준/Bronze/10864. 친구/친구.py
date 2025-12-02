import sys
input = sys.stdin.readline

n, m = map(int, input().split())
friends = {i:[] for i in range(1, n+1)}

for _ in range(m):
  a, b = map(int, input().split())
  friends[a].append(b)
  friends[b].append(a)

for k, v in friends.items():
  print(len(v))