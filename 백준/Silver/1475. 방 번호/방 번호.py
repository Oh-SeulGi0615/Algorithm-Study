import sys
input = sys.stdin.readline
import math

n = list(input().rstrip())

dict_ = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
for i in n:
    dict_[int(i)] += 1

if 6 in dict_ and 9 in dict_:
    dict_['6 or 9'] = math.ceil((dict_[6] + dict_[9]) / 2)
    dict_[6] = 0
    dict_[9] = 0

print(max(dict_.values()))