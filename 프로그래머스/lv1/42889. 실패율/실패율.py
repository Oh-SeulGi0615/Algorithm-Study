def solution(N, stages):
    stages.sort()
    fail_late = {i : 0 for i in range(1, N+1)}
    for i in range(1, N+1):
        if len(stages) > 0:
            fail_late[i] = stages.count(i) / len(stages)
            while i in stages:
                stages.remove(i)
        else:
            fail_late[i] = 0

    answer = sorted(fail_late.items(), key=lambda x : x[1], reverse=True)
    answer = [answer[i][0] for i in range(len(fail_late))]
    return answer