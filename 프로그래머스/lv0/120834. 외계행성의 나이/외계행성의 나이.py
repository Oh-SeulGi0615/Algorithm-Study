def solution(age):
    age_list = list(str(age))
    answer = [chr(int(i) + 97) for i in age_list]
    return ''.join(answer)