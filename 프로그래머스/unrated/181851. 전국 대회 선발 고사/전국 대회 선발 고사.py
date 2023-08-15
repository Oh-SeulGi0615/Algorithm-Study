def solution(rank, attendance):
    arr = [rank[i] for i in range(len(rank)) if attendance[i] == True]
    arr.sort()

    answer = 10000 * rank.index(arr[0]) + 100 * rank.index(arr[1]) + rank.index(arr[2])
    return answer