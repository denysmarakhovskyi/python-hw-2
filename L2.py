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


def smNumb(numb):
    tmpNumb = numb
    while tmpNumb > 9:
        tmpRest = 0
        while tmpNumb > 9:
            tmpRest += tmpNumb % 10
            tmpNumb //= 10
        tmpNumb += tmpRest
    return tmpNumb


print(smNumb(38) == 2)
print(smNumb(40) == 4)
print(smNumb(48) == 3)
print(smNumb(2) == 2)


def smNumb1(numb):
    tmpRest = 0
    while numb > 0:
        tmpRest += numb % 10
        numb = numb // 10

        if numb == 0 and tmpRest > 9:
            numb = tmpRest
            tmpRest = 0

    return tmpRest


def sumNumb(numb):
    if numb == 0:
        return 0
    if numb % 9 == 0:
        return 9
    return numb % 9


def commStr(str1, str2):
    resultStr = ''
    i = 0
    while i < len(str1):
        if str1[i] in str2 and str1[i] not in resultStr:
            resultStr += str1[i]
        i += 1
    return resultStr


commStr('loli', 'lali')


def commStr(str1, str2):
    resultStr = ''
    i = 0
    while i < len(str1):
        if str1[i].isalpha() in str2 and str1[i] not in resultStr:
            resultStr = resultStr + str1[i]
        i += 1
    return resultStr


def commStrArr(str1, str2):
    ressltArr = []
    for ch in str1:
        if ch.isalpha() and ch in str2 and ch not in ressltArr:
            ressltArr.append(ch)
    return ''.join(ressltArr)


print(commStr('1l\t olipfhidfhge', '1lolllllll\t lllllllllllooooooop'))

print(commStr('loli', 'luck') == 'l')
print(commStr('good day', 'good morning') == 'god')


def commStrSet(str1: str, str2):
    ressltSet = set()
    i = 0
    for ch in str1:
        i += 1
        if ch.isalpha() and ch in str2:
            ressltSet.add(ch)
    print(i)
    return ''.join(ressltSet)
