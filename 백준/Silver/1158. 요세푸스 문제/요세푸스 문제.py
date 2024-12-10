from collections import deque
n, m = map(int, input().split())

arr = deque(range(1, n+1))
answer = []
cnt = 1

while len(arr) > 0:
  if cnt == m:
    answer.append(arr.popleft())
    cnt = 1
  else:
    arr.append(arr.popleft())
    cnt += 1

print('<' + ', '.join(map(str, answer)) + '>')