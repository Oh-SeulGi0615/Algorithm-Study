import sys

visited = []
now_x, now_y = '', ''
valid = 'Valid'
for _ in range(36):
  loc = list(sys.stdin.readline().rstrip())
  x, y = loc[0], loc[1]

  if not now_x:
    now_x = x
    now_y = y
    visited.append([x, y])
  else:
    if (abs(ord(now_x) - ord(x)) + abs(int(now_y) - int(y)) != 3) or [x, y] in visited:
      valid = 'Invalid'
      break
    elif abs(ord(now_x) - ord(x)) == 0 or abs(int(now_y) - int(y)) == 0:
      valid = 'Invalid'
      break
    else:
      visited.append([x, y])
      now_x = x
      now_y = y

if (abs(ord(now_x) - ord(visited[0][0])) + abs(int(now_y) - int(visited[0][1])) != 3):
  valid = 'Invalid'

print(valid)