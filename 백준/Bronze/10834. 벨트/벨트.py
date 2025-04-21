m = int(input())

rotation = 1
direction = 0
for _ in range(m):
  a, b, s = map(int, input().split())

  rotation = int(rotation / a) * b

  if s == 1:
    if direction == 0:
      direction = 1
    else:
      direction = 0

print(direction, rotation)