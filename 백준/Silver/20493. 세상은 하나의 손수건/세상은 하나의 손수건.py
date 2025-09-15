n, t = map(int, input().split())
if n == 0:
  print(t, 0)
else:
  direction = [[1, 0], [0, -1], [-1, 0], [0, 1]]
  now_direction, time = 0, 0
  loc = [0, 0]
  for _ in range(n):
    s, d = input().split()
    
    loc[0] += direction[now_direction][0] * (int(s) - time)
    loc[1] += direction[now_direction][1] * (int(s) - time)
    time = int(s)

    if d == 'right':
      now_direction = (now_direction + 1) % 4
    elif d == 'left':
      now_direction = (now_direction + 3) % 4
  
  if time == t:
    print(*loc)
  else:
    loc[0] += direction[now_direction][0] * (t - time)
    loc[1] += direction[now_direction][1] * (t - time)
    print(*loc)