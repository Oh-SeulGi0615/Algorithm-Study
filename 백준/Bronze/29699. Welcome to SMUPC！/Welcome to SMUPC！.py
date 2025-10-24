import sys

string = 'WelcomeToSMUPC'
n = int(sys.stdin.readline())

print(string[(n % 14)-1])