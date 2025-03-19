t = int(input())
for _ in range(t):
  blank = input()
  n, m = map(int, input().split())
  sj = list(map(int, input().split()))
  sb = list(map(int, input().split()))

  if max(sj) >= max(sb):
    print('S')
  elif max(sj) < max(sb):
    print('B')