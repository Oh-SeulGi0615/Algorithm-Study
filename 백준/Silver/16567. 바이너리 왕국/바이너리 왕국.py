import sys
input = sys.stdin.readline

n, m = map(int, input().split())
road = [0] + list(map(int, input().split())) + [0]

cnt = 0
for i in range(n):
  if i == 0 and road[i] == 1:
    cnt += 1
  elif road[i] == 1 and road[i-1] == 0:
    cnt += 1

for _ in range(m):
  o = list(map(int, input().split()))

  if o[0] == 0:
    print(cnt)
  
  else:
    idx = o[1]

    if road[idx] == 0:
      road[idx] = 1

      if road[idx - 1] == 0 and road[idx + 1] == 0:
        cnt += 1
      elif road[idx - 1] == 1 and road[idx + 1] == 1:
        cnt -= 1