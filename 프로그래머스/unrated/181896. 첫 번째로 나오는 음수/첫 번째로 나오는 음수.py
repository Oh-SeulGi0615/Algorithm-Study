def solution(num_list):
    arr = []
    for i in range(len(num_list)):
        if num_list[i] < 0:
            arr.append([i, num_list[i]])
    
    if len(arr) == 0:
        return -1.
    else:
        return arr[0][0]