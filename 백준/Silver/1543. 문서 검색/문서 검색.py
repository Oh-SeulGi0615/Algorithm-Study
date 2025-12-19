import sys
input = sys.stdin.readline

doc = input().rstrip()
kw = input().rstrip()

cnt = 0
loc = 0
while True:
  if loc + len(kw) > len(doc):
    break
  
  if doc[loc:loc+len(kw)] == kw:
    doc = doc[loc+len(kw):]
    loc = 0
    cnt += 1
  else:
    loc += 1

print(cnt)