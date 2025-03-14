n = int(input())
arr = list(map(int, input().split()))

distance = 0
for i in arr:
  for j in arr:
    distance += abs(i - j)

print(distance)