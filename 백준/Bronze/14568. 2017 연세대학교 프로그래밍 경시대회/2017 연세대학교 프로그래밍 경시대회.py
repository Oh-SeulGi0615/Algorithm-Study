import sys
input = sys.stdin.readline

n = int(input())

cnt = 0
for i in range(1,n-4):
    for j in range(i+2,n-2):
        for k in range(2,n-2,2):
            if i + j + k == n:
                cnt += 1

print(cnt)