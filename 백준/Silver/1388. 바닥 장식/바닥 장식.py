import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]

visited = [[False for _ in range(m)] for _ in range(n)]

def dfs_h(visited, x, y, graph):
    if x<0 or y<0 or y >= n or x >= m:
        return 0
    if visited[y][x] == False and graph[y][x] == '-':
        visited[y][x] == True
        graph[y][x] = 0
        return dfs_h(visited, x+1, y, graph)
    return 0

def dfs_v(visited, x, y, graph):
    if x<0 or y<0 or y >= n or x >= m:
        return 0
    if visited[y][x] == False and graph[y][x] == '|':
        visited[y][x] == True
        graph[y][x] = 0
        return dfs_v(visited, x, y+1, graph)
    return 0
    
cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == '-':
            cnt += 1
            dfs_h(visited, j, i, graph)
        elif graph[i][j] == '|':
            cnt += 1
            dfs_v(visited, j, i, graph)

print(cnt)