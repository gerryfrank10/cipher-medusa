from os import path
import struct
def Ecaesar(msg, key):
    
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890./,:}{|][*&^%$!@)('
    translate =''
    if msg is None:
        print("The message cant be none")
        exit(0)
    if path.isfile(msg):
        with open(msg,'r') as fp:
            for line in fp.readlines():
                line = line.upper()
                for symbol in line:
                    if symbol in letters:
                        num = letters.find(symbol)
                        num = num + key
                        if num > len(letters):
                            num = num - len(letters)
                        elif num < 0:
                            num = num + len(letters)
                        translate = translate + letters[num]
                    else:
                        translate = translate + symbol
    else:
        msg = msg.upper()
        for symbol in msg:
            if symbol in letters:
                num = letters.find(symbol)
                num = num + key
                if num > len(letters):
                    num = num - len(letters)
                elif num < 0:
                    num = num + len(letters)
                translate = translate + letters[num]
            else:
                translate = translate + symbol
    return translate

def Dcaesar(msg, key):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890./,:}{|][*&^%$!@)('
    if msg == None:
        print ("There should be the text to decrypted")
        exit(0)
    translate = ''
    if path.isfile(msg):
        with open(msg, 'r') as fp:
            for line in fp.readline():
                line = line.upper()
                for symbol in line:
                    if symbol in letters:
                        num = letters.find(symbol)
                        num = num -key
                        if num < 0:
                            num = num + len(letters)
                        translate = translate + letters[num]
                    else:
                        translate = translate + symbol
    else:
        msg = msg.upper()
        for symbol in msg:
            if symbol in letters:
                num = letters.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(letters)
                translate = translate + letters[num]
            else:
                translate = translate + symbol
    return translate
