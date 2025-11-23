import sys
input = sys.stdin.readline

n, l = map(int, input().split())
arr = sorted(list(map(int, input().split())))

pipe = [False if i in arr else True for i in range(2001)]

cnt = 0
for i in range(1001):
    if pipe[i] == False:
        pipe[i:i+l] = [True] * l
        cnt += 1

print(cnt)