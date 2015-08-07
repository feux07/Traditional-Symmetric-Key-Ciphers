__author__ = 'Ahmfrkyvz'

def take_inverse(r1,r2):

    global s1,s2,s,t1,t2,t,q

    s1 = 1
    s2 = 0
    t1 = 0
    t2 = 1
    while not r2 == 0:
        r = r1 % r2
        q = (r1-r)/r2
        s = s1-q*s2
        t = t1-q*t2
        r1 = r2
        r2 = r
        s1 = s2
        s2 = s
        t1 = t2
        t2 = t

    return int(t1%26)

def gcd(x, y):
    if y == 0:
        return x
    else:
        r = x % y
        return gcd(y, r)

def multiplicative_cipher(plainText, key):
    i = 0
    encryptedText = ""

    if gcd(key,26) == 1:
        while i < len(plainText):
            char =  ord(plainText[i])
            if char >= 65 and char <= 90:
                char = (char%65 * key)%26 + 65

            elif char >= 97 and char <= 122:
                char = (char%97 * key)%26 + 97

            encryptedText += chr(char)
            i=i+1
        return encryptedText
    else:
        print("key is not a prime number in Z26...")
        return "Error: key is not a prime number in Z26..."

def decrypt_multiplicative_cipher(encryptedText, key):
    i = 0
    decryptedText = ""
    inverseOfKey = take_inverse(26,key)

    while i < len(encryptedText):
        char = ord(encryptedText[i])
        if char >= 65 and char <= 90:
            char = (char%65 * inverseOfKey)%26 + 65

        elif char >= 97 and char <= 122:
            char = (char%97 * inverseOfKey)%26 + 97

        decryptedText += chr(char)
        i=i+1
    else:
        return decryptedText

