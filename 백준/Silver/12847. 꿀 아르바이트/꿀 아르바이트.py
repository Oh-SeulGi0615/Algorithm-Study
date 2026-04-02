import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

add = [0]
for i in arr:
  add.append(add[-1] + i)

best = 0
for j in range(0, len(add)-m):
  wage = add[j+m] - add[j]
  if wage > best:
    best = wage

print(best)