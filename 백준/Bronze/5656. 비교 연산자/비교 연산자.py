import sys
input = sys.stdin.readline

def check(num1, num2, operator):
    if operator == '<':
        return bool(num1 < num2)
    elif operator == '<=':
        return bool(num1 <= num2)
    elif operator == '>':
        return bool(num1 > num2)
    elif operator == '>=':
        return bool(num1 >= num2)
    elif operator == '==':
        return bool(num1 == num2)
    elif operator == '!=':
        return bool(num1 != num2)

cnt = 1
while True:
    arr = list(input().split())
    if arr[1] == 'E':
        break

    n1, n2 = map(int, [arr[0], arr[-1]])

    if check(n1, n2, arr[1]) == True:
        print(f'Case {cnt}: true')
    else:
        print(f'Case {cnt}: false')
    
    cnt += 1