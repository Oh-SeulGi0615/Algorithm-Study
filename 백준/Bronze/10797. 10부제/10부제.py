import sys
input = sys.stdin.readline

a = int(input())

arr = list(map(int, input().split()))

cnt = 0
for i in arr:
    if i == a:
        cnt +=1

print(cnt)