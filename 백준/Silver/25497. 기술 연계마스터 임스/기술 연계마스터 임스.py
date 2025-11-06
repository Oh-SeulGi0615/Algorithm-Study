import sys
from collections import deque

n = int(sys.stdin.readline())
arr = deque(sys.stdin.readline().rstrip())

lr_stack, sk_stack = [], []
skill = 0
state = True

for _ in range(n):
    comp = arr.popleft()
    if comp not in ['L', 'R', 'S', 'K'] and state:
        skill += 1
    else:
        if comp == 'L':
            lr_stack.append(comp)
        elif comp == 'R':
            if not lr_stack:
                state = False
            elif lr_stack and state:
                lr_stack.pop()
                skill += 1

        elif comp == 'S':
            sk_stack.append(comp)
        elif comp == 'K':
            if not sk_stack:
                state = False
            elif sk_stack and state:
                sk_stack.pop()
                skill += 1

print(skill)