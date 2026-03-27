import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n = int(input())
  arr_n = list(map(int, input().split()))
  m = int(input())
  arr_m = list(map(int, input().split()))
  k = int(input())
  arr_k = list(map(int, input().split()))

  set58 = set()
  for a in arr_n:
    for b in arr_m:
      for c in arr_k:
        res = str(a + b + c)

        if all(char in ['5', '8'] for char in res):
          set58.add(res)
  print(len(set58))