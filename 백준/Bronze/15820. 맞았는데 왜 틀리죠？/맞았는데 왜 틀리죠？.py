import sys
input = sys.stdin.readline

s1, s2 = map(int, input().split())

answer1 = []
for _ in range(s1):
    a, b = map(int, input().split())
    if a != b:
        answer1.append(1)

if s2 != 0:
    answer2 = []
    for _ in range(s2):
        c, d = map(int, input().split())
        if c != d:
            answer2.append(1)

if len(answer1) == 0:
    if s2 != 0:
        if len(answer2) == 0:
            print('Accepted')
        else:
            print('Why Wrong!!!')
    else:
        print('Accepted')
else:
    print('Wrong Answer')