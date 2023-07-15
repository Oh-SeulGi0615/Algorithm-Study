import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dict1 = {}
for i in range(len(a)):
    try:
        dict1[a[i]] += 1
    except:
        dict1[a[i]] = 1
for j in range(len(b)):
    try:
        dict1[b[j]] += 1
    except:
        dict1[b[j]] = 1

cnt = 0
for a, b in dict1.items():
    if b == 1:
        cnt += 1

print(cnt)