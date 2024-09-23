n = int(input())
s = list(input().rstrip())

upper, lower, number, special = 0, 0, 0, 0

for char in s:
    if char.isdigit() == True:
        number += 1
    elif char.isalpha() == True:
        if 122 >= ord(char) >= 97:
            lower += 1
        elif 90 >= ord(char) >= 65:
            upper += 1
    elif char in list('!@#$%^&*()-+'):
        special += 1

print(max(6 - len(s), [upper, lower, number, special].count(0)))