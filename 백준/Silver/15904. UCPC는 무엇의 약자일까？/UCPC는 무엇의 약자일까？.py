import sys
input = sys.stdin.readline

str_ucpc = input().rstrip()
target = ['U','C','P','C']

result = ''
for i in range(len(str_ucpc)):
    if str_ucpc[i] in target:
        result += str_ucpc[i]

idx = 0
answer = ''
for x in result:
    if answer == 'UCPC':
        break
    elif x == target[idx]:
        answer += x
        idx += 1

if answer == 'UCPC':
    print('I love UCPC')
else:
    print('I hate UCPC')