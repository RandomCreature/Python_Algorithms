# По введенным пользователем координатам двух точек вывести уравнение прямой, проходящей через эти точки.

a = float(input('Введите целое число, абсциссу точки 1: '))
b = float(input('Введите целое число, ординату точки 1: '))
c = float(input('Введите целое число, асбциссу точки 2: '))
d = float(input('Введите целое число, ординату точки 2: '))
print('Координаты указанных точек: ', '[', a, ',',  b, ']', ', ', '[', c, ',', d, ']')
print('Искомое уравнение прямой для данных двух точек: ',
      'y = ', float((d - b)/(c - a)), 'x - ', float((a * d + b * c)/(c - a)))

