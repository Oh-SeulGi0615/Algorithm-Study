def solution(my_string, indices):
    arr = list(my_string)
    indices.sort()
    
    for i in indices[::-1]:
        arr.pop(i)
    answer = ''.join(arr)
    return answer