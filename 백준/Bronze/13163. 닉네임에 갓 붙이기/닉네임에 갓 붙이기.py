import sys
input = sys.stdin.readline

for _ in range(int(input())):
    nick = input().split()
    result = 'god' + ''.join(nick[1:])

    print(result)