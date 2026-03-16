import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

if n == 2:
  a = arr[0][1] // 2
  print(*[a, arr[0][1] - a])
else:
  a = (arr[0][1] + arr[0][2] - arr[1][2]) // 2

  res = [a]
  for i in range(1, n):
    ans = arr[0][i] - a
    res.append(ans)
  print(*res)