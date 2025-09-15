n = int(input())

arr = []
for _ in range(n):
  a, b = map(int, input().split())
  arr.append([a, b])

arr = sorted(arr, key=lambda x: (-x[0], -x[1]))

result = 0
for args in arr:
  result += args[0] * n + args[1]
  n -= 1

print(result)