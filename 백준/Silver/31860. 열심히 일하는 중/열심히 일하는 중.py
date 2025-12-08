import sys
input = sys.stdin.readline

import heapq

n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
result = []

for task in arr:
  heapq.heappush(result, -task)

amount = 0
day = 0
amount_list = []
while True:
  today = -heapq.heappop(result)
  if today <= k:
    break

  amount = int(amount / 2) + today
  amount_list.append(amount)

  heapq.heappush(result, -(today - m))
  day += 1

print(day)
print(*amount_list, sep='\n')