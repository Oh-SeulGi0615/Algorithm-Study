import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n = int(input())

  cnt_5 = 0
  idx = 5
  while idx <= n:
    cnt_5 += n // idx
    idx *= 5
  
  print(cnt_5)