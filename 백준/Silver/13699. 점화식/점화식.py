import sys
input = sys.stdin.readline

dict_ = {i:0 for i in range(36)}
dict_[0] = 1

n = int(input())

for i in range(1, n+1):
    for j in range(i):
        dict_[i] += dict_[j] * dict_[(i-1)-j]

print(dict_[n])