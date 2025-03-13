t, x, m = map(int, input().split())

min_time = 1e9
for _ in range(m):
  d, s = map(int, input().split())
  if d % s != 0:
    meet_time = d // s
  else:
    meet_time = (d // s) - 1
  
  if meet_time < min_time:
    min_time = meet_time

if min_time == 0:
  print(0)
elif t > min_time:
  print((min_time + (t - min_time)//2)*x)
else:
  print(t * x)