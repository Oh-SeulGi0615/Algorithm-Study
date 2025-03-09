import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()
length = 0

for _ in range(n):
    s = list(sys.stdin.readline().split())
    
    if s[0] == 'push':
        queue.append(int(s[1]))
        length += 1
    elif s[0] == 'pop':
        if queue:
            length -= 1
            print(queue.popleft())
        else:
            print(-1)
    elif s[0] == 'size':
        print(length)
    elif s[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif s[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif s[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)