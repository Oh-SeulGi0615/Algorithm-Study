import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

arr = list(map(int, list(str(a*b*c))))

dict_ = {i:0 for i in range(10)}

for i in arr:
    dict_[i] += 1

for j in dict_.values():
    print(j)