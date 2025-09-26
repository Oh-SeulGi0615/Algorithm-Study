t = int(input())
for _ in range(t):
  n = int(input())
  before = list(input())
  after = list(input())

  cnt = 0
  before_w = before.count('W')
  after_w = after.count('W')
  diff = [True if before[i] == after[i] else False for i in range(n)]

  if before_w == after_w:
    cnt += diff.count(False) // 2
    print(cnt)
  else:
    cnt += abs(after_w - before_w)
    remain = diff.count(False) - abs(after_w - before_w)
    if remain != 0:
      cnt += remain // 2
    print(cnt)