def solution(numbers):
    list_ = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(len(list_)):
        numbers = numbers.replace(list_[i], str(list_.index(list_[i])))
    return int(numbers)