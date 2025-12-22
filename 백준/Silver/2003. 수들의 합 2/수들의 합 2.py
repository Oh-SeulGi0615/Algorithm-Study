import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

sum_ = 0
sum_list = [0]
for num in arr:
  sum_ += num
  sum_list.append(sum_)

cnt = 0
start, end = 0, 0
while (start <= n) and (end <= n):
  res = sum_list[end] - sum_list[start]

  if res == m:
    cnt += 1
    end += 1
  elif res < m:
    end += 1
  else:
    start += 1

print(cnt)