import sys
input = sys.stdin.readline

cnt = 0
for i in range(1, int(input())+1):
    arr = list(map(int, list(str(i))))
    if i % sum(arr) == 0:
        cnt += 1

print(cnt)