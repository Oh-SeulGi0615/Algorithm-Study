import sys
input = sys.stdin.readline

n = int(input())

dict_ = {}
for i in range(1,n+1):
    s, c, l = map(int, input().split())
    dict_[i] = [s, c, l]

dict_ = sorted(dict_.items(), key= lambda x : (-x[1][0], x[1][1], x[1][2]))

print(dict_[0][0])