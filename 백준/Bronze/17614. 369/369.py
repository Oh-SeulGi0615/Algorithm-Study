import sys
input = sys.stdin.readline

arr = [str(i) for i in range(int(input())+1) if '3' in str(i) or '6' in str(i) or '9' in str(i)]

clap = 0
for i in arr:
    clap += i.count('3')
    clap += i.count('6')
    clap += i.count('9')

print(clap)