def solution(emergency):
    order = sorted(emergency)[::-1]
    answer = [order.index(i)+1 for i in emergency]
    return answer