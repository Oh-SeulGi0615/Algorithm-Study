import sys
input = sys.stdin.readline

n = int(input())

arr = [n]
res = 0
while arr:
  num = arr.pop()
  a = num // 2
  b = num - a

  res += a * b
  if a > 1:
    arr.append(a)
  if b > 1:
    arr.append(b)

print(res)