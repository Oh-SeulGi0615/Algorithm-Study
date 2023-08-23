def solution(array, commands):
    answer = []
    for i in commands:
        sliced_array = array[i[0]-1 : i[1]]
        sliced_array.sort()
        answer.append(sliced_array[i[2]-1])
    return answer