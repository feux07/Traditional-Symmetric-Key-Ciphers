__author__ = 'Ahmfrkyvz'

def vigerene_cipher(plainText, key):
    i = 0
    encryptedText = ""

    key = key.lower()
    plainText = plainText.replace('İ', 'i')
    plainText = plainText.lower()

    while i < len(plainText):

        char = ord(plainText[i])
        charOfKey = ord(key[i%(len(key))])

        if char >= 97 and char <= 122 and charOfKey >= 97 and charOfKey <= 122:
            encryptedText += chr((char + charOfKey - 2*97)%26 +97)
        else:
            encryptedText += chr(char)
        i=i+1

    return encryptedText

def decrypt_vigerene_cipher(encryptedText, key):
    i=0
    plainText = ""

    while i < len(encryptedText):

        char = ord(encryptedText[i])
        charOfKey = ord(key[i%(len(key))])

        if char >= 97 and char <= 122 and charOfKey >= 97 and charOfKey <= 122:
            plainText += chr((char - charOfKey)%26 + 97)
        else:
            plainText += chr(char)
        i=i+1

    return plainText
