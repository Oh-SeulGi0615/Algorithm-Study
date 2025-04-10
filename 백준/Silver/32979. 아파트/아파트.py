from collections import deque

n = int(input())
t = int(input())
arr = deque(list(map(int, input().split())))
b = list(map(int, input().split()))

result = []
for turn in b:
  for i in range(turn):
    d = arr.popleft()

    if i == turn - 1:
      result.append(d)
      arr.appendleft(d)
    else:
      arr.append(d)

print(*result)