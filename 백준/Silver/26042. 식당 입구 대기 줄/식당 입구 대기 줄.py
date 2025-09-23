from collections import deque

n = int(input())

queue = deque([])
len_q = 0
best_len = 0
s_n = 1e9

for _ in range(n):
  arr = list(map(int, input().split()))
  if arr[0] == 1:
    queue.append(arr[1])
    len_q += 1
  else:
    queue.popleft()
    len_q -= 1

  if len_q > best_len:
    best_len = len_q
    s_n = queue[-1]
  elif len_q == best_len and queue[-1] < s_n:
    s_n = queue[-1]

print(best_len, s_n)