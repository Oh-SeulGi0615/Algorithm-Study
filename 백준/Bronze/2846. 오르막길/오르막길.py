import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

max_height = 0
height = 0
for i in range(1, n):
  if arr[i] > arr[i-1]:
    height += arr[i] - arr[i-1]
    if max_height < height:
      max_height = height
  else:
      height = 0

print(max_height)