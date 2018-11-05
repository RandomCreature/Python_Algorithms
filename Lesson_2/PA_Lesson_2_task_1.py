# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
# а должна запрашивать новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0'
# в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.

while True:
    print('Elementary calculator. Simple operations with the numbers you enter, Your options: \n'
          '1. Addition. Enter "1"; \n'
          '2. Subtraction. Enter "2"; \n'
          '3. Multiplication. Enter "3"; \n'
          '4. Division. Enter "4"; \n'
          '5. Exit program. Enter "0".')

    # Getting user's input

    number_1 = float(input('Enter the first number here: '))
    number_2 = float(input('Enter the second number here: '))
    choice = int(input('Choose an option: '))


    def addition_f():
        return number_1 + number_2


    def subtraction_f():
        print(number_1 - number_2)


    def multiplication_f():
        print(number_1 * number_2)


    def division_f():
        if number_2 == 0:
            print('Division by 0! No more planes to fall!')
        else:
            print(number_1 / number_2)


    if choice == 0:
        break
    elif choice == 1:
        print(addition_f())
        continue
    elif choice == 2:
        print(subtraction_f())
        continue
    elif choice == 3:
        print(multiplication_f())
        continue
    elif choice == 4:
        print(division_f())
        continue
