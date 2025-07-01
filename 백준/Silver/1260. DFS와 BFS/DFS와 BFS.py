dfs_list, bfs_list = [], []
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    dfs_list.append(start)

    for node in graph[start]:
        if node not in visited:
            dfs(graph, node, visited)
    return visited

def bfs(graph, start):
    from collections import deque

    visited = set([start])
    queue = deque([start])

    while queue:
        node = queue.popleft()
        bfs_list.append(node)
        for next_node in graph[node]:
            if next_node not in visited:
                visited.add(next_node)
                queue.append(next_node)
    return visited

n, m, v = map(int, input().split())

graph = {i:[] for i in range(1, n+1)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
sorted_graph = {k:sorted(v) for k, v in graph.items()}

dfs(sorted_graph, v)
bfs(sorted_graph, v)

print(*dfs_list)
print(*bfs_list)