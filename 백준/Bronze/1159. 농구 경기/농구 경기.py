import sys
input = sys.stdin.readline

dict_ = {chr(i) : 0 for i in range(97, 123)}
for _ in range(int(input())):
    name = input().rstrip()
    dict_[name[0]] += 1

result = ''
for k, v in dict_.items():
    if v >= 5:
        result += k

if len(result) > 0:
    print(result)
else:
    print('PREDAJA')