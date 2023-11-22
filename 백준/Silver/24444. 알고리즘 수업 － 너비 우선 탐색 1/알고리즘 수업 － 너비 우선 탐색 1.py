import sys
input = sys.stdin.readline

from collections import deque

n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for j in range(1, n+1):
    if len(graph[j]) > 0:
        graph[j].sort()

visited = [0] * (n+1)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 1

    cnt = 2
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = cnt
                cnt += 1

bfs(graph, r, visited)

for k in range(1, n+1):
    print(visited[k])