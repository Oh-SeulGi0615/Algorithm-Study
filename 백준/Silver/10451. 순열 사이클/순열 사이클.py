import sys
sys.setrecursionlimit(2000)
def dfs(s, graph, visited):
    visited[s] = True
    for i in graph[s]:
      if visited[i] == False:
        dfs(i, graph, visited)

for _ in range(int(input())):
  n = int(input())
  arr = list(map(int, input().split()))

  graph = [[] for _ in range(n+1)]
  for i in range(1, n+1):
    graph[i].append(arr[i-1])
  
  cnt = 0
  visited = [False for _ in range(n+1)]
  for i in range(1, n+1):
    if visited[i] == False:
      cnt += 1
      dfs(i, graph, visited)

  print(cnt)