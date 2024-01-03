import sys
input = sys.stdin.readline

s1, s2, s3 = map(int, input().split())

dict_ = {i:0 for i in range(3, s1+s2+s3+1)}
for i in range(1, s1+1):
    for j in range(1, s2+1):
        for k in range(1, s3+1):
            dict_[i+j+k] += 1

dict_2 = sorted(dict_, key=lambda x: -dict_[x])

print(dict_2[0])