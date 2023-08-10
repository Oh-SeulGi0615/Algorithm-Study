def solution(num_list):
    
    sum1 = 1
    for i in range(len(num_list)):
        sum1  = sum1 * num_list[i]
        
    sum2 = sum(num_list) ** 2
    
    if sum1 > sum2:
        return 0
    elif sum1 < sum2:
        return 1