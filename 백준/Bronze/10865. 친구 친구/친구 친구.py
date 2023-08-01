import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dict_ = {i:0 for i in range(1,n+1)}
for _ in range(m):
    a, b = map(int, input().split())

    dict_[a] += 1
    dict_[b] += 1

for i in list(dict_.values()):
    print(i)