def solution(s):
    s_list = list(s)

    stack = []
    for i in range(len(s_list)):
        if len(stack) == 0 or s_list[i] == '(':
            stack.append(s_list[i])
        elif s_list[i] == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(s_list[i])

    if len(stack) == 0:
        return True
    else:
        return False