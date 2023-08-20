def solution(keyinput, board):
    max_x = [-1 * int((board[0] - 1) / 2), int((board[0] - 1) / 2)]
    max_y = [-1 * int((board[1] - 1) / 2), int((board[1] - 1) / 2)]

    answer = [0, 0]
    for i in keyinput:
        if i == 'up':
            if max_y[0] <= answer[1] < max_y[1]:
                answer[1] += 1
        elif i == 'down':
            if max_y[0] < answer[1] <= max_y[1]:
                answer[1] -= 1
        elif i == 'right':
            if max_x[0] <= answer[0] < max_x[1]:
                answer[0] += 1
        else:
            if max_x[0] < answer[0] <= max_x[1]:
                answer[0] -= 1
    return answer