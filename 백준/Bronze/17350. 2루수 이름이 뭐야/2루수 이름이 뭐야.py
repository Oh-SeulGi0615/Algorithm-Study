import sys
input = sys.stdin.readline

answer = 0
for _ in range(int(input())):
    player = input().rstrip()
    if 'anj' == player:
        answer = 1

if answer == 1:
    print('뭐야;')
else:
    print('뭐야?')