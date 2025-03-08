import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

stack = []
now = 1

while True:
    if a:
        if a[0] == now:
            a.pop(0)
            now += 1
        elif a[0] != now:
            if stack:
                if stack[-1] > a[0]:
                    stack.append(a.pop(0))
                elif stack[-1] == now:
                    stack.pop()
                    now += 1
                else:
                    print('Sad')
                    break
            else:
                stack.append(a.pop(0))
    elif (not a) and stack:
        if stack[-1] == now:
            stack.pop()
            now += 1
        elif stack[-1] != now:
            print('Sad')
            break
    elif (not a) and (not stack):
        print('Nice')
        break