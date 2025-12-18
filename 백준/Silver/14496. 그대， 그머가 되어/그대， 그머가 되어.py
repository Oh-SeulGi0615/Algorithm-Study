import sys
input = sys.stdin.readline

from collections import deque

a, b = map(int, input().split())
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [-1 for _ in range(n+1)]
visited[a] = 0

for _ in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

def bfs(graph, start, visited):
  queue = deque([start])

  while queue:
    v = queue.popleft()

    for i in graph[v]:
      if visited[i] == -1:
        queue.append(i)
        visited[i] = visited[v] + 1

bfs(graph, a, visited)
print(visited[b])