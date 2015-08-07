__author__ = 'Ahmfrkyvz'

key =[[ 9 , 7  , 11 , 13],
      [ 4 , 7  , 5  , 6 ],
      [ 2 , 21 , 14 , 9 ],
      [ 3 , 23 , 21 , 8 ]]

inverseKey =[[ 2  , 15 , 22 , 3 ],
             [ 15 , 0  , 19 , 3 ],
             [ 9  , 9  , 3  , 11],
             [ 17 , 0  , 4  , 7 ]]

def hill_cipher(plainText):
    i = 0
    c = 0
    matrix = [0 , 0 , 0 , 0]
    matrixIndex = [0 , 0 , 0 , 0]

    plainText = plainText.replace('İ', 'i')
    plainText = plainText.lower()
    encryptedText = plainText

    while i < len(plainText):
        char = ord(plainText[i])

        if char >= 97 and char <= 122:

            matrix[c] = char - 97
            matrixIndex[c] = i
            c+=1
            i+=1

            if c == 4:
                c = 0
                for j in range(0,4):
                    encryptedText = encryptedText[:matrixIndex[j]] \
                                    + chr((matrix[0]*key[0][j] + matrix[1]*key[1][j]
                                    + matrix[2]*key[2][j] + matrix[3]*key[3][j])%26 + 97) \
                                    + encryptedText[matrixIndex[j]+1:]
        else:
            i+=1

    return encryptedText

def decrypt_hill_cipher(encryptedText):
    i = 0
    c = 0
    matrix = [0 , 0 , 0 , 0]
    matrixIndex = [0 , 0 , 0 , 0]

    plainText = encryptedText

    while i < len(encryptedText):
        char = ord(encryptedText[i])

        if char >= 97 and char <= 122:

            matrix[c] = char - 97
            matrixIndex[c] = i
            c+=1
            i+=1

            if c == 4:
                c = 0
                for j in range(0,4):
                    plainText = plainText[:matrixIndex[j]] \
                                + chr((matrix[0]*inverseKey[0][j] + matrix[1]*inverseKey[1][j]
                                + matrix[2]*inverseKey[2][j] + matrix[3]*inverseKey[3][j])%26 + 97) \
                                + plainText[matrixIndex[j]+1:]
        else:
            i+=1

    return plainText
