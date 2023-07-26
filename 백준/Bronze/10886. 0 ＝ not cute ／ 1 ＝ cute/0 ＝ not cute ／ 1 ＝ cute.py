import sys
input = sys.stdin.readline

n = int(input())

cnt1, cnt2 = 0, 0
for _ in range(n):
    a = int(input())
    if a == 1:
        cnt1 += 1
    else:
        cnt2 += 1

if cnt1 > cnt2:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')