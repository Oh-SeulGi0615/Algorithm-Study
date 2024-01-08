import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
dict_ = {i:0 for i in range(1, 101)}

for _ in range(3):
    start, end = map(int, input().split())
    for i in range(start, end):
        dict_[i] += 1

cost = 0
for k, v in dict_.items():
    if v == 1:
        cost += a
    elif v == 2:
        cost += b * 2
    elif v == 3:
        cost += c * 3

print(cost)