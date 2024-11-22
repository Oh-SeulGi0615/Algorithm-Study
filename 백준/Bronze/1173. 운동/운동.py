n, m, M, t, r = map(int, input().split())

now = m
time = 0
while n > 0:
  if m + t > M:
    time = -1
    break
  elif m <= now + t <= M:
    now += t
    time += 1
    n -=1
  elif now + t > M:
    if now - r < m:
      now = m
    else:
      now -= r
    time += 1

print(time)