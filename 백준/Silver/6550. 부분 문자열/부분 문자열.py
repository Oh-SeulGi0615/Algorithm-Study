import sys
input = sys.stdin.readline

while True:
    try:
        s, t = input().split()

        no = 0
        for i in range(len(s)):
            if s[i] in t:
                t = t[t.index(s[i])+1 :]
            else:
                print('No')
                no = 1
                break
        if no == 0:
            print('Yes')
    except:
        break