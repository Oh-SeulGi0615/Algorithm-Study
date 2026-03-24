import sys
input = sys.stdin.readline

from collections import deque

n, k = map(int, input().split())

graph = [-1] * 100001
def bfs(graph, start):
  queue = deque([start])
  graph[start] = 0

  while True:
    v = queue.popleft()
    if v == k:
      break

    next = [v+1, v-1, v*2]
    for i in next:
      if 0 <= i <= 100000 and graph[i] == -1:
        queue.append(i)
        graph[i] = graph[v] + 1

bfs(graph, n)
print(graph[k])