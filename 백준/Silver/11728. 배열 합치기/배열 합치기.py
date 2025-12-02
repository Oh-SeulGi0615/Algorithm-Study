import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr_n = list(map(int, input().split()))
arr_m = list(map(int, input().split()))

idx_n, idx_m = 0, 0
result = []
while idx_n < n or idx_m < m:
  if idx_n >= n:
    result.append(arr_m[idx_m])
    idx_m += 1
  elif idx_m >= m:
    result.append(arr_n[idx_n])
    idx_n += 1

  elif arr_n[idx_n] < arr_m[idx_m]:
    result.append(arr_n[idx_n])
    idx_n += 1
  elif arr_n[idx_n] >= arr_m[idx_m]:
    result.append(arr_m[idx_m])
    idx_m += 1

print(*result)