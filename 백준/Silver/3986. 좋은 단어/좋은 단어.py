import sys
input = sys.stdin.readline

cnt = 0
for _ in range(int(input())):
    string = input().rstrip()

    if string.count('A') % 2 != 0 or string.count('B') % 2 != 0:
        continue
    else:
        stack = [string[0]]
        for i in range(1, len(string)):
            if len(stack) == 0:
                stack.append(string[i])
            elif string[i] != stack[-1]:
                stack.append(string[i])
            elif string[i] == stack[-1]:
                stack.pop()
        if len(stack) == 0:
            cnt += 1
print(cnt)