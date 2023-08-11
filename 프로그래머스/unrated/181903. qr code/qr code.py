def solution(q, r, code):
    arr = []
    for i in range(len(code)):
        if i % q == r:
            arr.append(code[i])
    answer = ''.join(arr)
    return answer