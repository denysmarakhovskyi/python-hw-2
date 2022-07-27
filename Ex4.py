import sys


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
