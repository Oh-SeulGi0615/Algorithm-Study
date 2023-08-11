def solution(my_string):
    arr = [0 for i in range(52)]
    
    for i in my_string:
        if i.isupper() == True:
            arr[(ord(i)-65)] += 1
        else:
            arr[(ord(i)-71)] += 1
    return arr