arr = [input() for _ in range(3)]

if arr[0].isnumeric() == True:
  num = int(arr[0])+3
elif arr[1].isnumeric() == True:
  num = int(arr[1])+2
elif arr[2].isnumeric() == True:
  num = int(arr[2])+1

if num % 3 == 0 and num % 5 == 0:
  print('FizzBuzz')
elif num % 3 == 0 and num % 5 != 0:
  print('Fizz')
elif num % 3 != 0 and num % 5 == 0:
  print('Buzz')
else:
  print(num)