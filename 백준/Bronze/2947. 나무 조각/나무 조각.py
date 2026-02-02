import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
while arr != [1, 2, 3, 4, 5]:
  for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
      arr[i], arr[i+1] = arr[i+1], arr[i]
      print(*arr)