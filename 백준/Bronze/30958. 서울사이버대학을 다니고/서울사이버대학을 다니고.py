n = int(input())
string = input().rstrip()

dict_ = {chr(i) : 0 for i in range(97, 123)}

for char in string:
    if char.isalpha() == True:
        dict_[char] += 1

print(max(list(dict_.values())))