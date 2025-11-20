import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n = int(input())
  arr = list(map(int, input().split()))

  days = 1
  today, tomorrow = arr, []
  while sum(today) <= n:
    days += 1

    for i in range(6):
      next_eat = today[i] + today[(i-1)%6] + today[(i+1)%6] + today[(i+3)%6]
      tomorrow.append(next_eat)
    today = tomorrow
    tomorrow = []
  
  print(days)