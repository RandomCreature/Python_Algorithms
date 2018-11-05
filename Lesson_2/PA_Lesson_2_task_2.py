# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

number = str(input('Enter any integer: '))

even = []
odd = []
for i in number:
    if number.index(i) % 2 == 0:
        even.append(i)
    elif number.index(i) % 2 == 1:
        odd.append(i)
print(len(even))
print(even)
print(len(odd))
print(odd)
