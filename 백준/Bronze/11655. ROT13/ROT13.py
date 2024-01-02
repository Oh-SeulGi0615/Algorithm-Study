import sys
input = sys.stdin.readline

string = input().rstrip()

result = ''
for i in string:
    if 97 <= ord(i) <= 122:
        char = ord(i) + 13
        if char > 122:
            char -= 26
        result += chr(char)
    
    elif 65 <= ord(i) <= 90:
        char = ord(i) + 13
        if char > 90:
            char -= 26
        result += chr(char)

    else:
        result += i

print(result)