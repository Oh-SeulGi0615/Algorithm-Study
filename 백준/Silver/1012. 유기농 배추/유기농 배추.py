import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    def dfs(x, y):
        if x <= -1 or x >= m or y <= -1 or y >= n:
            return False
        if graph[y][x] == 1:
            graph[y][x] = 0
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)
            return True
        return False

    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(j, i) == True:
                result += 1

    print(result)