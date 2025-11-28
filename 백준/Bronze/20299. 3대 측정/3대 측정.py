import sys
input = sys.stdin.readline

n, k, l = map(int, input().split())

pass_team = 0
pass_member = []
for _ in range(n):
  arr = list(map(int, input().split()))

  if sum(arr) < k:
    continue

  if any(num < l for num in arr):
    continue

  pass_team += 1
  pass_member.extend(arr)

print(pass_team)
print(*pass_member)