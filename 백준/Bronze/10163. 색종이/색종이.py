import sys
place = [[0 for _ in range(1001)] for _ in range(1001)]

n = int(sys.stdin.readline())
if n == 0:
  print(0)
else:
  for i in range(1, n+1):
    arr = list(map(int, sys.stdin.readline().split()))
    start = arr[:2]
    width, height = arr[3], arr[2]

    for h in range(start[0], start[0]+height):
      for w in range(start[1], start[1]+width):
        place[h][w] = i
  
  flat_place = sum(place, [])
  for j in range(1, n+1):
    print(flat_place.count(j))