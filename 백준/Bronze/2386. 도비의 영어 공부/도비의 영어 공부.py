import sys
input = sys.stdin.readline

while True:
    string = input().rstrip()
    if string == '#':
        break
    
    string_list = string.split()
    char = string_list[0]

    arr = []
    for i in string_list[1:]:
        arr.extend(list(i.lower()))

    cnt = 0
    for j in arr:
        if j == char:
            cnt += 1
    
    print(f'{char} {cnt}')