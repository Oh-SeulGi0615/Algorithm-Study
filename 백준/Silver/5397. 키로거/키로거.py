import sys
input = sys.stdin.readline

for _ in range(int(input())):
    stack = list(input().rstrip())

    left, right = [], []
    for i in stack:
        if i == '<':
            if len(left) > 0:
                right.append(left.pop())
        elif i == '>':
            if len(right) > 0:
                left.append(right.pop())
        elif i == '-':
            if len(left) > 0:
                left.pop()
        else:
            left.append(i)
    
    result = ''.join(left) + ''.join(right[::-1])
    print(result)