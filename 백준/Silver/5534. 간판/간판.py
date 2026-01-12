import sys
input = sys.stdin.readline

n = int(input())
name = input().rstrip()

cnt = 0
for _ in range(n):
  old = input().rstrip()

  found = False
  for i in range(len(old)):
    if not found:
      if old[i] == name[0]:
        for k in range(1, len(old[i:])):
          word = ''
          for j in range(i, min(i+(k*(len(name)-1))+1, len(old)), k):
            word += old[j]

          if word == name:
            found = True
  if found:
    cnt += 1

print(cnt)