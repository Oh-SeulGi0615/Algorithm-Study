import sys
from collections import deque
queue = deque()
a, b, c = [], [], []

for _ in range(int(sys.stdin.readline())):
  arr = list(map(int, sys.stdin.readline().split()))

  if arr[0] == 1:
      queue.append([arr[1], arr[2]])
  
  elif arr[0] == 2:
    if queue[0][1] == arr[1]:
      a.append(queue[0][0])
      queue.popleft()
    else:
      b.append(queue[0][0])
      queue.popleft()

if queue:
  c = [i[0] for i in queue]

a, b, c = sorted(a), sorted(b), sorted(c)

for x in (a, b, c):
    print(*(x if x else ["None"]))