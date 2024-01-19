def check(arr1, arr2):
    for i, j in zip(arr1, arr2):
        if i != j:
            return 'No'
    return 'Yes'

for _ in range(int(input())):
    string = list(input().lower())

    print(check(string, string[::-1]))