n = int(input())
arr = list(map(int, input().split()))

total_point = 0
rage = 0
for i in arr:
  if i == 1:
    rage += 1
    total_point += rage
  else:
    rage -= 1
    total_point += rage

print(total_point)