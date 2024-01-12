import sys
input = sys.stdin.readline

for _ in range(int(input())):
    string = input().rstrip()

    if string[0] == 'P':
        print('skipped')
    else:
        arr = list(map(int, string.split('+')))
        print(sum(arr))