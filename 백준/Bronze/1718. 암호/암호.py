import sys
input = sys.stdin.readline

string = list(input().rstrip())
secret_key = list(input().rstrip())

charset = [chr(i) for i in range(96, 123)]

result = ''
for i in range(len(string)):
    if string[i] == ' ':
        result += ' '
    else:
        char = ord(string[i]) - charset.index(secret_key[i % len(secret_key)])

        if char < 97:
            result += chr(123 - (97 - char))
        else:
            result += chr(char)

print(result)