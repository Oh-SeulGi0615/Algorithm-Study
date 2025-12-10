import sys
input = sys.stdin.readline

n = int(input())
arr = [(i*(i+1)//2) for i in range(100)]
case_ = list(set([arr[a]+arr[b]+arr[c] for a in range(1, len(arr)) for b in range(1, len(arr)) for c in range(1, len(arr)) if arr[a]+arr[b]+arr[c] <= 1000]))

for _ in range(n):
  k = int(input())
  if k in case_:
    print(1)
  else:
    print(0)