import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]

def dfs_h(x, y):
    if x<0 or y<0 or y >= n or x >= m:
        return 0
    if graph[y][x] == '-':
        graph[y][x] = 0
        return dfs_h(x+1, y)
    return 0

def dfs_v(x, y):
    if x<0 or y<0 or y >= n or x >= m:
        return 0
    if graph[y][x] == '|':
        graph[y][x] = 0
        return dfs_v(x, y+1)
    return 0
    
cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == '-':
            cnt += 1
            dfs_h(j, i)
        elif graph[i][j] == '|':
            cnt += 1
            dfs_v(j, i)

print(cnt)