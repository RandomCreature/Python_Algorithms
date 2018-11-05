# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

print('Here\'s the row: 1 -0.5 0.25 -0.125 ...')
elms = int(input('Enter the number of the elements for the row above to find its total: '))


start = 1  # Determining the first number of the row
counter = 0  # Setting variable counter to count the number of iterations
total = 0  # Setting the initial amount of the row's sum


while counter < elms:
    total += start
    start = start / -2
    counter += 1


print(total)

