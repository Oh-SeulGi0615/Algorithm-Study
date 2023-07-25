import sys
input = sys.stdin.readline

cnt = 0
while True:
    a = input().rstrip()
    if a == '':
        break
    cnt += 1
    
print(cnt)