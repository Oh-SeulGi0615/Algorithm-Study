from bisect import bisect_left

def func(arr):
  lis = []
  for comp in arr:
    idx = bisect_left(lis, comp)
    if idx == len(lis):
      lis.append(comp)
    else:
      lis[idx] = comp
  return len(lis)

n = int(input())
arr = list(map(int, input().split()))

print(func(arr))