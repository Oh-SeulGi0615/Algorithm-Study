import sys
from collections import deque

n = int(sys.stdin.readline())
string = list(sys.stdin.readline().rstrip())

q = int(sys.stdin.readline())
for _ in range(q):
  l, r = map(int, sys.stdin.readline().split())

  left = deque(string[l-1:r])
  right = deque([0] * len(left))

  best = 0
  for _ in range(len(left)):
    left.appendleft(0)
    right.append(left.pop())
    right.popleft()

    score = 0
    for i in range(len(right)):
      if left[i] != 0 and right[i] != 0 and left[i] == right[i]:
        score += 1

    if score > best:
      best = score
  
  print(best)