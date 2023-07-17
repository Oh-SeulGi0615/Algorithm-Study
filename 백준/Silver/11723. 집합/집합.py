import sys
input = sys.stdin.readline

n = int(input())
s = []

for _ in range(n):
    l = list(input().split())
    
    if len(l) == 2:
        a = l[0]
        b = int(l[1])
    else:
        a = l[0]

    if a == 'add' and b not in s:
        if type(s) == list:
            s.append(b)
        else:
            s.add(b)
    if a == 'remove' and b in s:
        s.remove(b)
    if a == 'check':
        if b in s:
            print(1)
        else:
            print(0)
    if a == 'toggle':
        if b in s:
            s.remove(b)
        else:
            if type(s) == list:
                s.append(b)
            else:
                s.add(b)
    if a == 'all':
        s = [i for i in range(1,21)]
    if a == 'empty':
        s = []