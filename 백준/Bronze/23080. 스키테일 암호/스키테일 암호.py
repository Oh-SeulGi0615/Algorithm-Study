import sys
input = sys.stdin.readline

n = int(input())
pwd = list(input())

list_ = [pwd[i] for i in range(0, len(pwd), n)]
print(''.join(list_))