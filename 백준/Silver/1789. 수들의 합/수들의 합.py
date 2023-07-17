import sys
input = sys.stdin.readline

n = int(input())

sum = 1
cnt = 1
while True:
    cnt += 1
    sum += cnt
    if sum > n:
        break
    
print(cnt - 1)