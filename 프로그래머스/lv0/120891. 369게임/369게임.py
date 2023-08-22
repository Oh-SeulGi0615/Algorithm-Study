def solution(order):
    order_list = list(str(order))
    answer = 0
    for i in order_list:
        if int(i) in [3, 6, 9]:
            answer += 1
    return answer