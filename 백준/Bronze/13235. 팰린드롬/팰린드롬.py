import sys
input = sys.stdin.readline

string = input().rstrip()

result = 0
for i, j in zip(string, string[::-1]):
    if i != j:
        result = 1

if result == 1:
    print('false')
else:
    print('true')