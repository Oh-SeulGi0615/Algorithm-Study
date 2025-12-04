import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

status = 'up'
result = 'YES'
for i in range(1, n):
  if status == 'up':
    if arr[i-1] < arr[i]:
      continue
    elif arr[i-1] > arr[i]:
      status = 'down'
    else:
      result = 'NO'
      break
  
  elif status == 'down':
    if arr[i-1] < arr[i]:
      result = 'NO'
      break
    elif arr[i-1] > arr[i]:
      continue
    else:
      result = 'NO'
      break

print(result)