import sys
input = sys.stdin.readline

for _ in range(int(input())):
    arr = input().split()
    n1, n2, result2 = map(int, [arr[0], arr[2], arr[-1]])
    
    if arr[1] == '+':
        result1 = n1 + n2
    elif arr[1] == '-':
        result1 = n1 - n2
    elif arr[1] == '*':
        result1 = n1 * n2
    else:
        result1 = int(n1 / n2)

    if result1 == result2:
        print('correct')
    else:
        print('wrong answer')