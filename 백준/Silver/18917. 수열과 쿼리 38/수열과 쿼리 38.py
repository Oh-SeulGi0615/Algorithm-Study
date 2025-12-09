import sys
input = sys.stdin.readline

m = int(input())

xor = [0]
sum = 0
for _ in range(m):
    query = list(map(int, input().split()))

    if query[0] == 1:
        xor.append(xor[-1] ^ query[1])
        sum += query[1]
    elif query[0] == 2:
        xor.append(xor[-1] ^ query[1])
        sum -= query[1]
    elif query[0] == 3:
        print(sum)
    else:
        print(xor[-1])