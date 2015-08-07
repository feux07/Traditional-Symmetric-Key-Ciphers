__author__ = 'Ahmfrkyvz'

def delete_newline(text):
    i=1
    while text[-i] == '\n':
        i+=1
    text = text[:len(text)-i+1]
    return text

def rail_fence_cipher(plainText):
    evenText = ""
    oddText = ""

    plainText = delete_newline(plainText)

    i = 0
    while i < len(plainText):
        evenText += plainText[i]
        i+=2

    i = 1
    while i < len(plainText):
        oddText += plainText[i]
        i+=2

    encryptedText = evenText + oddText

    return encryptedText

def decrypt_rail_fence_cipher(encryptedText):

    i = 0
    plainText = ""

    encryptedText = delete_newline(encryptedText)
    index = int(len(encryptedText)/2)
    
    if len(encryptedText)%2 == 0:
        while i < index:
            plainText += encryptedText[i] + encryptedText[i + index]
            i+=1
    else:
        while i < index:
            plainText += encryptedText[i] + encryptedText[i + index + 1]
            i+=1
        plainText += encryptedText[i]
        
    return plainText
