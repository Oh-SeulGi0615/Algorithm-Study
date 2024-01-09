import sys
input = sys.stdin.readline

string = list(input().rstrip())

joi, ioi = 0, 0
for i in range(len(string) - 2):
    if string[i] + string[i+1] + string[i+2] == 'JOI':
        joi += 1
    elif string[i] + string[i+1] + string[i+2] == 'IOI':
        ioi += 1

print(joi, ioi, sep='\n')