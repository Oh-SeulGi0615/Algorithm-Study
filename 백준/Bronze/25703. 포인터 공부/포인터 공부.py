import sys
input = sys.stdin.readline

n = int(input())

def pointer(num):
    print('int a;')

    for i in range(1, n+1):
        if i == 1:
            print('int *ptr = &a;')
        elif i == 2:
            print('int ' + '*'*i + f'ptr{i} = &ptr;')
        else:
            print('int ' + '*'*i + f'ptr{i} = &ptr{i-1};')

pointer(n)