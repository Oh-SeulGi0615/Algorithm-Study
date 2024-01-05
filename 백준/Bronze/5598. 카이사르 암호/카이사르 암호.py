import sys
input = sys.stdin.readline

string = input().rstrip()

result = ''
for i in string:
    if i == 'A': result += 'X'
    elif i == 'B': result += 'Y'
    elif i == 'C': result += 'Z'
    else: result += chr(ord(i) - 3)

print(result)