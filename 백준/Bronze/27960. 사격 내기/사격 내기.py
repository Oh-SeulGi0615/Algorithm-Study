import sys
input = sys.stdin.readline

a, b = map(int, input().split())

a2 = int(bin(a)[2:])
b2 = int(bin(b)[2:])
sum_ = a2 + b2

result = 0
for i in range(len(list(str(sum_))[::-1])):
    if list(str(sum_))[::-1][i] == '1':
        result += 2 ** i

print(result)