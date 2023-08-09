import sys
input = sys.stdin.readline

str_ = input().rstrip()

list = []
for i in range(len(str_)):
    if str_[i] == str.upper(str_[i]):
        list.append(str.lower(str_[i]))
    else:
        list.append(str.upper(str_[i]))

print(''.join(list))