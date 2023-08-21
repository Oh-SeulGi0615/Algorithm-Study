def solution(my_string):
    import re
    arr = re.sub('[^0-9]',' ',my_string).split(' ')

    answer = 0
    for i in arr:
        if i != '':
            answer += int(i)
    return answer