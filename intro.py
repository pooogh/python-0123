import math # math.round()
from math import ceil as c
from math import *
'''
a = 10
b = 5
print(a / b)
print(a // b)
print(float(a % 3), end=', ')
print('text', 5, sep='...')

name = input('Enter your name: ')
print('Hello, ' + name)
age = input('Your age: ')
print('Age:', int(age), type(age))
'''

# name = input('Enter your name: ')

# if name == 'Oleg':
#     print('Oleg the best!!!')
# elif name == 'Bogdar':
#     print('You are wonderful!!!')
# else:
#     print('Hello, ' + name)

# age = int(input())

# if 0 < age <= 18:
#     print('You are young')
# elif age <= 30 or age > 35:
#     print('Oleg')
# # not a !a

# i = 0
# while i <= 3:
#     print(i)
#     i += 1

# string = 'Hello, Oleg'
# for j in string: # for (let i = 0, i <= 10, i += 1)
#     print(j)

# for i in range(2, 20, 2):
#     print(i)

# for i in range(20, 2, -2):
#     print(i)

# улиточка Дима ползет вверх по веточке на n см в день, ночью Дима спит, поэтому 
# сползает по веточке вниз на m см. за сколько суток улиточка Дима полностью 
# заберется на верх веточки длиной x см.


# любитель геометрии Павел задал двоечнику Даниле задачу: 
# - вот тебе листок бумаги, Данила, размером n x m
# - и что мне с ним делать, Павел?
# - посчитай, сколько квадартов может получиться из этого листочка,  Данила, 
# если сторона квадрата будет равна самой короткой стороне листочка
# - ты адекватный, Павел, а ниче что....
# 20 х 8 -> 8 x 8 (1 s) 12 x 8 -> 8 x 8 (2s) 4 x 8 -> 8 x 8 (2s) 4 x 4 (1s) 4 x 4

def squares(n, m):
    mn = min(n, m)
    mx = max(n, m)
    count = 0
    while mn != 0:
        print(mx, mn, count)
        count += mx // mn
        mx %= mn # mx = mx % mn
        temp = mx
        mx = max(mx, mn)
        mn = min(temp, mn)
    return count

print(squares(8, 8))
def f_name(x: int, y: int) -> int:
    """Function multiply numbers"""
    print('function f_name')
    return x * y

f_name(2, 3)
# print(f_name)

def power(x, y=2):
    return x ** y

power(y=3, x=3)

def f_2(*args):
    print(args)
    print(type(args))

f_2(1, 2, 'text', False)

arr = [1, 2, 3]
first, *tail = arr
*tail2, last = arr
arr_2 = [1, 2, 3, 4, 5]
first_1, *tail, last_1 = arr_2
print(first_1, last_1)
print(tail, tail2)

def hello(**args):
    print('Hello,', args['name'])

hello(surname='Kulkov', name='Oleg')

def inter(name):
    print(f'Hello, {name}')

inter('Bogdar')

def f_3():
    pass

'''
дана шахматная доска
на вход функция принимает координаты двух клеток шахматной доски
определите, являются ли эти клетки клетками одного цвета (true/false)
'''

'''
дана шахматная доска
дается две координаты клетки: начальная и конечная
определите, может ли конь попасть из начальной клетки в конечную за 1 ход
'''

'''
дана шоколадка размером n x m квадратиков
определите, можно ли разделив ее 1 раз вдоль или поперек получить кусочек,
состоящий ровно из k квадратиков
'''

'''
Илья Николаич плавает в бассейне размером n x m
Илья Николаич устал
Илья Николаич хочет жить
Илья Николаич находится на расстоянии x от одной из длинных стен (не обязательно ближайшей)
Илья Николаич находится на расстоянии y от одной из коротких стен (не обязательно ближайшей)
Илья Николаич не хочет оказаться на дне, сколько минимально метров нужно проплыть
Илье Николаичу, чтобы выжить
'''

'''
дано число n
выведите в терминал (выпуклый) треугольник из чисел от 1 до n 
пример:
n = 4
1
12
123
1234
123
12
1

1234
123
12
1
12
123
1234
'''