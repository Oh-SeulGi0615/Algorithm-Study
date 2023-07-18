import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

cost = {'Y':0, 'M':0}

for i in arr:
    a = i // 30
    cost['Y'] += (a+1) * 10

    b = i // 60
    cost['M'] += (b+1) * 15

if cost['Y'] < cost['M']:
    print('Y', cost['Y'])
elif cost['Y'] > cost['M']:
    print('M', cost['M'])
else:
    print('Y', 'M', cost['Y'])