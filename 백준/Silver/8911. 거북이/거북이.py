t = int(input())
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
now = 0

for _ in range(t):
  orders = list(input())

  loc = [0, 0]
  max_x, max_y, min_x, min_y = 0, 0, 0, 0

  for order in orders:
    if order == 'F':
      loc[0] += direction[now][0]
      loc[1] += direction[now][1]
    elif order == 'B':
      loc[0] -= direction[now][0]
      loc[1] -= direction[now][1]
    elif order == 'L':
      now = (now + 3) % 4
    elif order == 'R':
      now = (now + 1) % 4
    
    if loc[0] > max_x: max_x = loc[0]
    elif loc[0] < min_x: min_x = loc[0]
    elif loc[1] > max_y: max_y = loc[1]
    elif loc[1] < min_y: min_y = loc[1]
  
  extent = abs(max_x - min_x) * abs(max_y - min_y)
  print(extent)