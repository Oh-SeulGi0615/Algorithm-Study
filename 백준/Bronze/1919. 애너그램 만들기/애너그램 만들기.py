import sys
input = sys.stdin.readline

string1 = input().rstrip()
string2 = input().rstrip()

dict1 = {chr(i):0 for i in range(97, 123)}
dict2 = {chr(i):0 for i in range(97, 123)}

for i in range(len(string1)):
    dict1[string1[i]] += 1
for j in range(len(string2)):
    dict2[string2[j]] += 1

result = 0
for k, v in dict1.items():
    if dict1[k] != dict2[k]:
        result += abs(dict1[k] - dict2[k])

print(result)