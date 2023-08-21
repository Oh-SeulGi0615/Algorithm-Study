def solution(s):
    s_dict = {}
    for i in s:
        if i not in s_dict:
            s_dict[i] = 1
        else:
            s_dict[i] += 1

    s_list = [i for i in s_dict if s_dict[i] == 1]
    s_list.sort()

    answer = ''.join(s_list)
    return answer