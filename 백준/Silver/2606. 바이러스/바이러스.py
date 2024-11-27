c = int(input())

graph = [[] for _ in range(c+1)]
infest = [False for _ in range(c+1)]

def dfs(g, s, visited):
  visited[s] = True
  for i in g[s]:
    if not visited[i]:
      dfs(g, i, visited)

for _ in range(int(input())):
  a, b = map(int, input().split())
  
  graph[a].append(b)
  graph[b].append(a)

dfs(graph, 1, infest)
print(infest.count(True)-1)