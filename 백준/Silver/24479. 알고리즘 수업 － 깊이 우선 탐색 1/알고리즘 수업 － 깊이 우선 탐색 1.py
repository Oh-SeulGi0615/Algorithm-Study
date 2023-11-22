import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

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
cnt = 1

def dfs(graph, v, visited):
    global cnt
    visited[v] = cnt
    cnt += 1

    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i, visited)

dfs(graph, r, visited)

for k in range(1, n+1):
    print(visited[k])