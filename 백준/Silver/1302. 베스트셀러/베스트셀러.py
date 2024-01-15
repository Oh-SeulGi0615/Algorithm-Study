import sys
input = sys.stdin.readline

dict_ = {}
for _ in range(int(input())):
    name = input().rstrip()
    if name not in dict_:
        dict_[name] = 1
    else:
        dict_[name] += 1

list_ = sorted(dict_.keys(), key=lambda x: (-dict_[x], x))

print(list_[0])