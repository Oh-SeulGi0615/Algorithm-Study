import sys
input = sys.stdin.readline

string = input().rstrip()

for i in ['apa', 'epe', 'ipi', 'opo', 'upu']:
    string = string.replace(f'{i}', f'{i[0]}')

print(string)