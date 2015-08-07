__author__ = 'Ahmfrkyvz'

def caesar_cipher(plainText, key):
    i = 0
    encryptedText = ""

    while i < len(plainText):
        char =  ord(plainText[i])
        if char >= 65 and char <= 90:
            char = (char%65 + key)%26 + 65

        elif char >= 97 and char <= 122:
            char = (char%97 + key)%26 + 97

        encryptedText += chr(char)
        i=i+1
    return encryptedText

def decrypt_caesar_cipher(encryptedText, key):
    i = 0
    decryptedText = ""
    while i < len(encryptedText):
        char = ord(encryptedText[i])
        if char >= 65 and char <= 90:
            char = (char%65 - key)%26 + 65

        elif char >= 97 and char <= 122:
            char = (char%97 - key)%26 + 97

        decryptedText += chr(char)
        i=i+1
    else:
        return decryptedText
