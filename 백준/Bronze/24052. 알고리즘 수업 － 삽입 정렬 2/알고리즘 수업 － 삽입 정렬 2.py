import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

def insertion_sort(arr: list, cnt: int):
  writes = 0
  for i in range(1, n):
    loc = i - 1
    new_item = arr[i]

    while (0 <= loc and new_item < arr[loc]):
      arr[loc + 1] = arr[loc]
      writes += 1
      if writes == cnt:
        return arr[:]
      loc -= 1
    
    if (loc + 1) != i:
      arr[loc + 1] = new_item

      writes += 1
      if writes == cnt:
        return arr[:]
  
  return [-1]
  
print(*insertion_sort(arr, k))