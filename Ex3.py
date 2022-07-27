import sys


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

