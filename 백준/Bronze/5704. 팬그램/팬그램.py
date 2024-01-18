import sys
input = sys.stdin.readline

while True:
    string = input().rstrip()
    if string == '*':
        break

    dict_ = {chr(i):0 for i in range(97, 123)}

    for char in string:
        if char != ' ':
            dict_[char] += 1

    if 0 in list(dict_.values()):
        print('N')
    else:
        print('Y')