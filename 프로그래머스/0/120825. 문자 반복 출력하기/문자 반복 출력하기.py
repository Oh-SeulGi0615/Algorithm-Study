def solution(my_string, n):
    answer = [char * n for char in my_string]
    return ''.join(answer)