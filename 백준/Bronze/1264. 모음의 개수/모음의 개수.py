import sys
input = sys.stdin.readline

list_ = ['a','e','i','o','u','A','E','I','O','U']

while True:
    a = input().rstrip()
    if a == '#':
        break

    cnt = 0
    for i in list(a):
        if i in list_:
            cnt += 1
    
    print(cnt)
