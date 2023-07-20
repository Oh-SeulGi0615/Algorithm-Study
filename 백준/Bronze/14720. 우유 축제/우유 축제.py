import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

cnt = []
for i in range(n):
    if 0 not in cnt:
        if arr[i] == 0:
            cnt.append(0)
    elif cnt[-1] == 0:
        if arr[i] == 1:
            cnt.append(1)
    elif cnt[-1] == 1:
        if arr[i] == 2:
            cnt.append(2)
    elif cnt[-1] == 2:
        if arr[i] == 0:
            cnt.append(0)
        
print(len(cnt))