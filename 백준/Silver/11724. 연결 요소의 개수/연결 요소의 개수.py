import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    if v not in graph[u]:
        graph[u].append(v)
    if u not in graph[v]:
        graph[v].append(u)

def dfs(graph, v, visited):
    visited[v] = True
    arr.append(v)

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

connected_component = []
for j in range(1, n+1):
    visited = [False] * (n+1)
    arr = []
    dfs(graph, j, visited)

    arr.sort()
    if arr not in connected_component:
        connected_component.append(arr)

print(len(connected_component))