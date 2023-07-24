import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    cnt1, cnt2 = 0, 0
    for _ in range(n):
        p1, p2 = map(str, input().split())

        if p1 == 'R':
            if p2 == 'R':
                pass
            elif p2 == 'S':
                cnt1 += 1
            elif p2 == 'P':
                cnt2 += 1
        elif p1 == 'S':
            if p2 == 'R':
                cnt2 += 1
            elif p2 == 'S':
                pass
            elif p2 == 'P':
                cnt1 += 1
        elif p1 == 'P':
            if p2 == 'R':
                cnt1 += 1
            elif p2 == 'S':
                cnt2 += 1
            elif p2 == 'P':
                pass
    
    if cnt1 > cnt2:
        print('Player 1')
    elif cnt1 < cnt2:
        print('Player 2')
    else:
        print('TIE')