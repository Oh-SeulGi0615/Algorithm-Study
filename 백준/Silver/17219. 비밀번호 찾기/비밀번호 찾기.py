import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dict_ = {}
for _ in range(n):
    site, pwd = input().split()
    dict_[site] = pwd

for _ in range(m):
    site2 = input().rstrip()
    print(dict_[site2])