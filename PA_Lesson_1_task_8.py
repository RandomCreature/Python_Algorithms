# Определить, является ли год, который ввел пользователем, високосным или не високосным.

year = int(input('Введите год. Если Вы вводите год до Р.Х., добавьте перед ним знак "-": '))

if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
    print('Год високосный.')
else:
    print('Год не високосный.')
