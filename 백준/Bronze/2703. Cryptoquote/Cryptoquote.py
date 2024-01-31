import sys
input = sys.stdin.readline

for _ in range(int(input())):
    string = input().rstrip()
    char = input().rstrip()

    dict_ = {chr(i):'' for i in range(65, 91)}
    for i in range(len(char)):
        dict_[chr(i+65)] = char[i]

    result = ''
    for c in string:
        if c == ' ':
            result += ' '
        else:
            result += dict_[c]
    
    print(result)