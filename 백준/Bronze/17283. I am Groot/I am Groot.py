import sys

l = int(sys.stdin.readline())
r = int(sys.stdin.readline())

total_cm = l
now_branch = l
cnt = 0

while True:
  now_branch = int(now_branch * (r / 100))

  if now_branch <= 5:
    break
  
  cnt += 1
  total_cm += (2 ** cnt) * now_branch

print(total_cm - l)