def solution(str1, str2):
    list1 = list(str1)
    list2 = list(str2)
    
    result = []
    for i in range(len(list1)):
        result.append(list1[i])
        result.append(list2[i])
        
    answer = ''.join(result)
    return answer