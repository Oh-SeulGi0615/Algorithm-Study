def solution(a, d, included):
    arr = []
    
    for i in range(len(included)):
        if included[i] == True:
            sum_ = a + (d * i)
            arr.append(sum_)
            
    return sum(arr)