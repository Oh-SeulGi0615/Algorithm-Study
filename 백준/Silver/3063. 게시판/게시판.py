import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
  arr = list(map(int, input().split()))
  x1, y1, x2, y2 = arr[0], arr[1], arr[2], arr[3]
  x3, y3, x4, y4 = arr[4], arr[5], arr[6], arr[7]

  area1 = (x2 - x1) * (y2 - y1)

  if x2 <= x3 or x4 <= x1 or y2 <= y3 or y4 <= y1:
    print(area1)
  else:
    area2 = (min(x4, x2) - max(x3, x1)) * (min(y4, y2) - max(y3, y1))
    print(area1 - area2)