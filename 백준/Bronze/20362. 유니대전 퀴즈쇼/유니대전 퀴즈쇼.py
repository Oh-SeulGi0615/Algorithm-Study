import sys

n, s = sys.stdin.readline().rstrip().split()

cnt = True
answer = ''
list_ = []
for _ in range(int(n)):
  nickname, comment = sys.stdin.readline().rstrip().split()
  if nickname == s:
    answer = comment
    cnt = False
  
  if cnt == True:
    list_.append(comment)

print(list_.count(answer))