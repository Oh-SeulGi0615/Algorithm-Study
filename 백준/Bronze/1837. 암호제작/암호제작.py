import sys
input = sys.stdin.readline

a, b = map(int, input().split())

arr = []
for i in range(2,b):
    if a % i == 0:
        arr.append(i)

if len(arr) == 0:
    print('GOOD')
else:
    print('BAD', min(arr))