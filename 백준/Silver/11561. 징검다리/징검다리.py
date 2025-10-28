import sys

n = int(sys.stdin.readline())
for _ in range(n):
  num = int(sys.stdin.readline())

  if num != 1:
    high, low = int((2*num)**0.5), 1
    result = 0
    while high >= low:
      mid = (high + low) // 2
      if ((mid)*(mid+1))//2 <= num:
        result = mid
        low = mid + 1
      else:
        high = mid - 1
    print(result)
  else:
    print(1)