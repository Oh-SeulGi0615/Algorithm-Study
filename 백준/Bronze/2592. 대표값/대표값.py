import sys
input = sys.stdin.readline

arr = [int(input()) for _ in range(10)]

dict_ = {}
for i in arr:
    if i not in dict_.keys():
        dict_[i] = 1
    else:
        dict_[i] += 1

dict_ = sorted(dict_, key=lambda x : dict_[x])[::-1]

print(int(sum(arr) / len(arr)))
print(dict_[0])