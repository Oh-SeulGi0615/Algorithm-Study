import sys
input = sys.stdin.readline

def check(num, arr = list):
    result = num
    while True:
        if result % 26 == 0:
            arr.append(26)
            a = result // 26 - 1
        else:
            a, mod = divmod(result, 26)
            arr.append(mod)
        
        if a < 26:
            arr.append(a)
            break
        result = a

    return arr[::-1]

while True:
    string = input().rstrip()
    if string == 'R0C0':
        break

    char = string.split('C')

    row = int(char[0][1:])
    cell = int(char[-1])
    
    result = ''
    arr = []
    for num in check(cell, arr):
        if num != 0:
            result += chr(num + 64)
    
    print(result + str(row))