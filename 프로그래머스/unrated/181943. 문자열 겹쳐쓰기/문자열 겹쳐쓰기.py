def solution(my_string, overwrite_string, s):
    if len(my_string[s:]) <= len(overwrite_string):
        answer = ''.join([my_string[:s], overwrite_string])
        return answer
    else:
        answer = ''.join([my_string[:s], overwrite_string, my_string[s+len(overwrite_string):]])
        return answer