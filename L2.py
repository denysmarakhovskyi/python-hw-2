num = int(input())


def oddOrEven(num):
    if num % 2 == 0:
        print('Число Х є парним')
    else:
        print('Число Х є непарним')
    return 0


print(oddOrEven(num))


print('\n')


str = 'Testing string', 'Lux', 'up', 'Luxery'


def transformStr(str):
    if str[0] == 'L' and str[0] == 'l':
        print(str)
    elif str[0] == 'U' and str[0] == 'u':
        print(str)
    elif len(str) >= 5:
        print(str+'...')


print(transformStr(str))



transformStr('Testing string')  # 'Testi...' (довжина більше 5 символів)
transformStr('Lux')  # 'lux' (Починается на L)
transformStr('up')  # 'UP' (Починается на U)
transformStr('Luxery')  # 'luxer...' (Починается на L + довжина більше 5 символів)
