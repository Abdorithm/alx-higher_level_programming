#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) <= ord('z') and ord(str[i]) >= ord('a'):
            str = str.replace(str[i], chr(ord(str[i]) + (ord('A') - ord('a'))))
    print("{}".format(str))
