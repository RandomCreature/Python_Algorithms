# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
# чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.

import random

x = random.randint(0, 100)
counter = 0

while counter <= 10:
    user_try = int(input('Enter any number in range 0 to 100: '))
    user_try = user_try
    counter = counter + 1
    if user_try < x:
        print('The hidden number is larger!')
        continue
    elif user_try > x:
        print('The hidden number is smaller!')
        continue
    else:
        print('You win!')
        break

print(x)
