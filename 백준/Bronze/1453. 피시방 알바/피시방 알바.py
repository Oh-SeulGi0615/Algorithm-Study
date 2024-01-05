import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dict_ = {i:0 for i in range(1, 101)}
cnt = 0

for i in arr:
    if dict_[i] == 0:
        dict_[i] = 1
    else:
        cnt += 1

print(cnt)