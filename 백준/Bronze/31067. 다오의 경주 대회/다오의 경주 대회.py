import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

res = [arr[0]]
cnt = 0

for i in range(1, len(arr)):
  if cnt != -1:
    if arr[i] > res[-1]:
      res.append(arr[i])
    
    elif arr[i] + k > res[-1]:
      res.append(arr[i]+k)
      cnt += 1
    
    elif arr[i] + k <= res[-1]:
      cnt = -1
  
  else:
    break

print(cnt)