'''
1-5. https://github.com/vv31415926/python_lessons_02_LIte
6. Найти сумму цифр числа.
7. Найти произведение цифр числа.
8. Дать ответ на вопрос: есть ли среди цифр числа 5?
9. Найти максимальную цифру в числе
10. Найти количество цифр 5 в числе
'''


print( '-------- 6 ---------' )
num = input( 'введите число: ')
lst = num.split('.')
lst[0] = int( lst[0] )
if len(lst) > 1:
    lst[1] = int(lst[1]) if len(lst[1]) > 0 else 0

sum = 0
for ni in lst:
    while ni > 0:
        sum += ni % 10
        ni = ni // 10

print( 'сумма цифр {} равна: {}'.format( num, sum ) )


print( '-------- 7 ---------' )
num = input( 'введите число: ')
lst = num.split('.')
lst[0] = int( lst[0] )
if len(lst) > 1:
    lst[1] = int(lst[1]) if len(lst[1]) > 0 else 0

p = 1
for ni in lst:
    while ni > 0:
        p *= ni % 10
        ni = ni // 10

print( 'Произведение цифр {} равна: {}'.format( num, p ) )

print( '-------- 8 ---------' )
num = input( 'введите число: ')
s = 'в числе {} нет 5'.format(num)
for ch in num:
    if ch == '5':
        s = 'в числе {} есть 5'.format(num)
        break
print(s)

print( '-------- 9 ---------' )
num = input( 'введите число: ')
nMax=0
for ch in num:
    if ch != '.':
        if int(ch) > nMax:
            nMax = int( ch )
print('Максимальная цифра {}: {}'.format(num,nMax))


print( '-------- 10 ---------' )
num = input( 'введите число: ')
n5 = 0
for ch in num:
    if ch == '5':
        n5 += 1
print('В числе {} количество цифр 5 равно {}'.format(num,n5))

