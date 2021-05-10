
# 1. арифметическое элементов массива, переданного ей в качестве
# аргумента.

'''
m = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def mass(m):
    return print(int(sum(m) / len(m)))
mass(m)
'''

# 2. Написать функцию, которая определяет количество разрядов
# введенного целого числа. ( разряд это единицы, десятки,
# сотни, тысячи)

'''
def discharge(n):
    i = 0
    while n > 0:
        n = n//10
        i += 1
    return i
num = abs(int(input('Введите число: ')))
print('Количество разрядов: ', discharge(num))
'''

# 3. Напишите функцию, которая складывает цифры целого числа

'''
def summ(s):
    x = 0
    for i in s:
        x += int(i)
    return  s, '=', x
y = input('Введите число: ')
print('сумма числа', summ(y))
'''

# 4. Написать функцию month_to_season(), которая принимает 1
# аргумент - номер месяца - и возвращает название сезона, к
# которому относится этот месяц.
# 5. Например, передаем 2, на выходе получаем 'Зима'.
'''
def seasons(month):
    season_ranges = {(12, 1, 2): 'Зима',(3, 4, 5): 'Весна',(6, 7, 8): 'Лето',(9, 10, 11): 'Осень'}
    season = None
    for key, value in season_ranges.items():
        if month in key:
            season = value
            break
    return season
print(seasons(10))
'''

# 5. Написать функцию, которая определяет есть ли в списке
# дубликаты.
'''
def double():
    a = [10, 10, 23, 10, 123, 66, 78, 123]
    counter = {}
    for elem in a:
        counter[elem] = counter.get(elem, 0) + 1
    doubles = {element: count for element, count in counter.items() if count > 1}
    return print(doubles)
double()
'''

