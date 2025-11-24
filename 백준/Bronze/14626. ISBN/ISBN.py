import sys
input = sys.stdin.readline

isbn = list(map(lambda x: int(x) if x.isnumeric() else x, list(input().rstrip())))

sum_ = 0
loc_star = 0
for i in range(len(isbn)-1):
  if isbn[i] == '*':
    if i % 2 == 0:
      loc_star = 1
    else:
      loc_star = 3

  else:
    if i % 2 == 0:
      sum_ += isbn[i]
    else:
      sum_ += isbn[i] * 3

for num in range(10):
  if (sum_ + (loc_star * num) + isbn[-1]) % 10 == 0:
    print(num)