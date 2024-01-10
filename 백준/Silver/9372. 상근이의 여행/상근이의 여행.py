import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n+1)
    cnt = 0

    def dfs(graph, v, visited):
        visited[v] = True
        global cnt

        for i in graph[v]:
            if visited[i] == False:
                cnt += 1
                dfs(graph, i, visited)
    
    dfs(graph, 1, visited)
    print(cnt)