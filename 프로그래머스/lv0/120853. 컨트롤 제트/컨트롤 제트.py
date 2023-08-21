def solution(s):
    s_list = list(s.split())

    answer = 0
    for i in range(len(s_list)):
        if s_list[i] != 'Z':
            answer += int(s_list[i])
        else:
            answer -= int(s_list[i-1])
    return answer