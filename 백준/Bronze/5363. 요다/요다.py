import sys
input = sys.stdin.readline

for _ in range(int(input())):
    string = input().split()
    yoda = string[2:] + string[:2]

    print(*yoda)