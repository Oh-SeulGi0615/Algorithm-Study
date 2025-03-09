import sys
from collections import deque

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
c = list(map(int, sys.stdin.readline().split()))

queue = deque()
for i in range(n):
    if a[i] == 0:
        queue.append(b[i])

result = []
for j in range(m):
    queue.appendleft(c[j])
    result.append(queue.pop())

print(*result)