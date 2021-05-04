def calculator(a, b, sign):
    #a = int(input('first number:'))
    #b = int(input('second number:'))
    #sign = input('enter sign:')

    if sign == '+':
        print('a + b =', a + b)
    if sign == '-':
        print('a - b =', a - b)
    if sign == '*':
        print('a * b =', a * b)
    if sign == '/':
        print('a / b =', int(a / b))

calculator(7, 5, '*')

