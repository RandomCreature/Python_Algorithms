# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

number = int(input('Enter any integer number: '))
mirror_number = 0

while number > 0:
    last_digit = number % 10  # getting the last digit of user's enter (the 1st one for the new number)
    number = number // 10  # removing the last digit
    mirror_number = mirror_number * 10  # enlarging the last digit's scale
    mirror_number = mirror_number + last_digit  # Joining the last digits to the new number

print(mirror_number)
