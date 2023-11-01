import sys
input = sys.stdin.readline

mbti = list(input().rstrip())

answer = ''
for i in mbti:
    if i == 'E':
        answer += 'I'
    elif i == 'I':
        answer += 'E'
    elif i == 'S':
        answer += 'N'
    elif i == 'N':
        answer += 'S'
    elif i == 'T':
        answer += 'F'
    elif i == 'F':
        answer += 'T'
    elif i == 'J':
        answer += 'P'
    else:
        answer += 'J'
print(answer)