a = bin(int(input()))[2:]
b = bin(int(input()))[2:]
c = bin(int(input()))[2:]

pw = ''
if len(a) < 4:
    pw += '0' * (4 - len(a)) + a
else:
    pw += a[-4:]

if len(b) < 4:
    pw += '0' * (4 - len(b)) + b
else:
    pw += b[-4:]

if len(c) < 4:
    pw += '0' * (4 - len(c)) + c
else:
    pw += c[-4:]

print(str(int(pw, 2)).zfill(4))