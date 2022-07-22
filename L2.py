num = int(input())


def oddOrEven(num):
    if num % 2 == 0:
        print('Число є парним')
    else:
        print('Число є непарним')


print(oddOrEven(num))

print('\n')

str = str(input('Enter string: '))


def string(str):
    fiveSymbols = (str[0:5] + "...")
    if len(str) > 5:
        print(fiveSymbols)
    elif str.startswith('u') or 'U':
        print(str.upper())
    elif str.startswith('l') or 'L':
        print(str.lower())
    else:
        print(str)


print(string(str))
