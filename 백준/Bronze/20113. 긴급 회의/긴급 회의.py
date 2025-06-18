n = int(input())
arr = list(map(int, input().split()))

dict_ = {i:0 for i in range(1, n+1)}
for elem in arr:
    if elem == 0:
        continue
    dict_[elem] += 1
    
if list(dict_.values()).count(max(list(dict_.values()))) == 1:
    print(list(dict_.values()).index(max(list(dict_.values())))+1)
else:
    print('skipped')