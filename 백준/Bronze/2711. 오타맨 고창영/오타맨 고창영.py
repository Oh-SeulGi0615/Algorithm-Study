import sys
input = sys.stdin.readline

for _ in range(int(input())):
    num, string = map(str, input().split())
    num = int(num)

    if num == 1:
        string = string[1:]
    elif num == len(string):
        string = string[:-1]
    else:
        string = string[0:num-1] + string[num:]
    
    print(string)