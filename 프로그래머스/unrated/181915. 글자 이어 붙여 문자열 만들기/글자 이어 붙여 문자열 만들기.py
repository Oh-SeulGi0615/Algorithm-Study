def solution(my_string, index_list):
    list_ = []
    for i in index_list:
        list_.append(my_string[i])
    answer = ''.join(list_)
    return answer