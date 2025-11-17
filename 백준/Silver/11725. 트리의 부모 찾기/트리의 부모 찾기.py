import sys
sys.setrecursionlimit(10**5+1)

n = int(sys.stdin.readline())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
  a, b = map(int, sys.stdin.readline().split())
  tree[a].append(b)
  tree[b].append(a)

parent = {i:0 for i in range(2, n+1)}

visited = [False] * (n+1)
def dfs(graph, v, visited):
  visited[v] = True
  for i in tree[v]:
    if not visited[i]:
      parent[i] = v
      dfs(graph, i, visited)

dfs(tree, 1, visited)
print(*parent.values(), sep='\n')