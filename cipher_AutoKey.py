__author__ = 'Ahmfrkyvz'

def autokey_cipher(plainText, key):
    i = 0
    encryptedText=""

    plainText = plainText.replace('İ', 'i')
    plainText = plainText.lower()

    keyText = chr(key + 97) + plainText

    while i<len(plainText):
        charIndex = ord(plainText[i])
        keyIndex = ord(keyText[i])

        if charIndex >= 97 and charIndex <= 122 and keyIndex >= 97 and keyIndex <= 122:
            encryptedText += chr((charIndex + keyIndex - 2*97)%26 +97)
        else:
            encryptedText += chr(charIndex)
        i+=1
    return encryptedText

def decrypt_autokey_cipher(encryptedText, key):

    i=0
    decryptedText=""

    while i<len(encryptedText):

        charIndex = ord(encryptedText[i])
        keyIndex = key + 97

        if charIndex >= 97 and charIndex <= 122 and keyIndex >= 97 and keyIndex <= 122:
            key = (charIndex - keyIndex)%26
            decryptedText += chr(key + 97)
        else:
            decryptedText += chr(charIndex)
            key = charIndex - 97
        i+=1

    return decryptedText

