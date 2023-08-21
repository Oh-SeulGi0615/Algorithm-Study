def solution(my_string):
    str_list = list(my_string)

    str_dict = {}
    for i in str_list:
        if i not in str_dict:
            str_dict[i] = 1
        else:
            pass

    answer = ''.join(str_dict.keys())
    return answer