import sys
input = sys.stdin.readline

for _ in range(int(input())):
    p, m = map(int, input().split())

    sit = {i:0 for i in range(1, m+1)}

    fail = 0
    for _ in range(p):
        a = int(input())
        if sit[a] == 0:
            sit[a] = 1
        else:
            fail += 1
    
    print(fail)