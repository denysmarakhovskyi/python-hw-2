import sys


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

