def solution(l, r):
    import re
    result = []
    for i in range(l, r+1):
        a = str(i)
        b = re.sub('[^05*]', '', a)

        if len(b) > 0 and a == b:
            result.append(int(a))

    result = list(set(result))
    result.sort()

    if len(result) > 0:
        if result[0] == 0:
            result.pop(0)
        return result
    else:
        return [-1]