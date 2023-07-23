import sys
input = sys.stdin.readline

a = list(input().rstrip())

k, y = ['K','O','R','E','A'], ['Y','O','N','S','E','I']

for i in range(len(a)):
    if a[i] == k[0]:
        k.remove(a[i])
        if len(k) == 0:
            print('KOREA')
            break
        
    elif a[i] == y[0]:
        y.remove(a[i])
        if len(y) == 0:
            print('YONSEI')
            break