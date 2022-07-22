import sys

# a = int(input('Chose operation number: '))
# if a == 1:
#
# elif a == 2:
#
# else:
#     print('Operation have not been chosen')
#
#
# num = int(input())


def oddOrEven(num):
    if num % 2 == 0:
        print(f'Число {num} є парним')
    # elif num == str:
    #     return 0
    else:
        print(f'Число {num} є непарним')


oddOrEven(1)
oddOrEven(20)


def transStr(string: str):
    transedStr = string
    if len(string) > 5:
        transedStr = transedStr[0:5] + '...'
    if transedStr[0] in 'Uu':
        transedStr = transedStr.lower()
    elif transedStr[0] in 'Ll':
        transedStr = transedStr.upper()
    print(transedStr)


transStr('Testing string')
transStr('Lux')
transStr('up')
transStr('Luxery')


def sumNum(num):
    return num

print(sumNum(38) == 2)
print(sumNum(40) == 4)
print(sumNum(48) == 3)
print(sumNum(2) == 2)
