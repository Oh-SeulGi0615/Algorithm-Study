import sys
import heapq
q = []

for _ in range(int(sys.stdin.readline())):
  x = int(sys.stdin.readline())

  if x == 0:
    if len(q) > 0:
      print(heapq.heappop(q) * -1)
    else:
      print(0)
  else:
    heapq.heappush(q, -x)