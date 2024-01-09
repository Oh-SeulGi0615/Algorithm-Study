import sys
input = sys.stdin.readline

from collections import deque

n, m, l = map(int, input().split())

dict_ = {i:0 for i in range(1, n+1)}
queue = deque([i for i in range(1, n+1)])

cnt = 0
while True:
    dict_[queue[0]] += 1
    if m in list(dict_.values()):
        break

    cnt += 1
    
    if dict_[queue[0]] % 2 == 1:
        queue.rotate(-1 * l)
    else:
        queue.rotate(l)

print(cnt)