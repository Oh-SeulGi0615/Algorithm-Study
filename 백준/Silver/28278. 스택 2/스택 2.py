import sys
n = int(sys.stdin.readline())

stack = []
length = 0
for _ in range(n):
    a = list(map(int, sys.stdin.readline().split()))

    if a[0] == 1:
        stack.append(a[1])
        length += 1

    elif a[0] == 2:
        if stack:
            p = stack.pop()
            length -= 1
            print(p)
        else:
            print(-1)

    elif a[0] == 3:
        print(length)

    elif a[0] == 4:
        if stack:
            print(0)
        else:
            print(1)

    elif a[0] == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)