n, m = map(int, input().split())
arr = list(map(int, input().split()))

max_count = sum(arr) - n
if m > max_count:
  print('OUT')
else:
  print('DIMI')