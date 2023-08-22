def solution(s):
    s_list = list(s.split(' '))

    answer = []
    for j in s_list:
        arr = ''
        for k in range(len(j)):
            if k % 2 == 0:
                arr += j[k].upper()
            else:
                arr += j[k].lower()
        answer.append(arr)
    return ' '.join(answer)
