def solution(s, n):
    arr2 = [chr(i) for i in range(65,91)]
    arr3 = [chr(i) for i in range(97,123)]

    answer = ''
    for i in s:
        if i in arr2:
            if i == 'Z':
                answer += arr2[-1 + n]
            else:
                answer += arr2[(arr2.index(i) + n) % 26]
        elif i in arr3:
            if i == 'Z':
                answer += arr3[-1 + n]
            else:
                answer += arr3[(arr3.index(i) + n) % 26]
        else:
            answer += ' '
    return answer