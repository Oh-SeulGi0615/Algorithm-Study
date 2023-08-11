def solution(my_string, queries):
    list_ = list(my_string)
    for i in range(len(queries)):
        list_[queries[i][0]:queries[i][1]+1] = list_[queries[i][0]:queries[i][1]+1][::-1]
    
    answer = ''.join(list_)
    return answer