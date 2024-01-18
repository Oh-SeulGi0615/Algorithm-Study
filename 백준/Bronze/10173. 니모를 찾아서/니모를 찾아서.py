import sys
input = sys.stdin.readline

while True:
    string = input().rstrip()
    if string == 'EOI':
        break

    string = string.lower().replace(',','').split()
    if 'nemo' in string:
        print('Found')
    else:
        print('Missing')