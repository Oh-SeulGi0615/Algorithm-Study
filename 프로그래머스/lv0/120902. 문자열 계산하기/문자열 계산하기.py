def solution(my_string):
    my_string_list = list(my_string.split())

    answer = int(my_string_list[0])
    for i in range(1, len(my_string_list)-1):
        if i % 2 == 1:
            if my_string_list[i] == '+':
                answer += int(my_string_list[i+1])
            else:
                answer -= int(my_string_list[i+1])
    return answer