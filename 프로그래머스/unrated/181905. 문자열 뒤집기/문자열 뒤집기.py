def solution(my_string, s, e):
    arr = list(my_string)
    arr[s:e+1] = arr[s:e+1][::-1]
    
    answer = ''.join(arr)
    return answer