import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = list(map(int, input().split()))

arr = sorted(arr)
s, e = 0, n-1
cnt = 0
while s < e:
  if arr[s] + arr[e] == m:
    cnt += 1
    s += 1
    e -= 1
  elif arr[s] + arr[e] > m:
    e -= 1
  elif arr[s] + arr[e] < m:
    s += 1

print(cnt)