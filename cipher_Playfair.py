__author__ = 'Ahmfrkyvz'

playfairKey = [['l' , 'g' , 'd' , 'b' , 'a'],
               ['q' , 'm' , 'h' , 'e' , 'c'],
               ['u' , 'r' , 'n' , 'i' , 'f'],
               ['x' , 'v' , 's' , 'o' , 'k'],
               ['z' , 'y' , 'w' , 't' , 'p']]

def find_column_index(matrix, char): #sutun indeksi

    row = -1
    for i in matrix:
        row = row+1
        column = -1
        for j in i:
            column = column+1
            if j == char:
                return column

def find_row_index(matrix, char): #satir indeksi

    row = -1
    for i in matrix:
        row = row+1
        column = -1
        for j in i:
            column = column+1
            if j == char:
                return row

def playfair_cipher(plainText, paddingChar):
    i = 0
    c = 0
    char = [' ', ' ']
    indexChar = [0, 0]

    plainText = plainText.replace('İ', 'i')
    plainText = plainText.lower()
    plainText = plainText.replace('j', 'i')


    while(i < len(plainText)):#if the two letters in a pair are the same a paddingChar is inserted to separate them.

        if ord(plainText[i]) >= 97 and ord(plainText[i]) <= 122:
            char[c] = plainText[i]
            c+=1
            if c == 2:
                if char[0] == char[1]:
                    plainText = plainText[:i] + paddingChar + plainText[i:]
                    i+=1
                char[0] = char[1]
                c =1
            i+=1
        else:
            i+=1
    i = 0
    c = 0
    while(i < len(plainText)):#count latin character in the  plaintext.
        if ord(plainText[i]) >= 97 and ord(plainText[i]) <= 122:
            c+=1
        i+=1
    if c%2 == 1:#if the number of characters in the plaintext is odd, one extra paddingChar is added at the end.
        plainText += paddingChar

    encryptedText = plainText

    i = 0
    c = 0
    while i < len(plainText):

        if ord(plainText[i]) >= 97 and ord(plainText[i]) <= 122:
            char[c] = plainText[i]
            indexChar[c] = i
            c+=1
            i+=1
            if c == 2:
                char1_Row = find_row_index(playfairKey, char[0])
                char1_Column = find_column_index(playfairKey, char[0])
                char2_Row = find_row_index(playfairKey, char[1])
                char2_Column = find_column_index(playfairKey, char[1])

                if char1_Row == char2_Row:
                    char[0] = playfairKey[char1_Row][(char1_Column + 1)%5]
                    char[1] = playfairKey[char2_Row][(char2_Column + 1)%5]
                elif char1_Column == char2_Column:
                    char[0] = playfairKey[(char1_Row + 1)%5][char1_Column]
                    char[1] = playfairKey[(char2_Row + 1)%5][char2_Column]
                else:
                    char[0] = playfairKey[char1_Row][char2_Column]
                    char[1] = playfairKey[char2_Row][char1_Column]

                encryptedText = encryptedText[:indexChar[0]] + char[0] + encryptedText[indexChar[0]+1:indexChar[1]] \
                                + char[1] + encryptedText[indexChar[1]+1:]
                c = 0
        else:
            i+=1

    return encryptedText

def decrypt_playfair_cipher(encryptedText):
    i = 0
    c = 0
    char = ['x', 'x']
    indexC = [0, 0]
    decryptedText = encryptedText

    while i < len(encryptedText):

        if ord(encryptedText[i]) >= 97 and ord(encryptedText[i]) <= 122:
            char[c] = encryptedText[i]
            indexC[c] = i
            c+=1
            i+=1

            if c == 2:
                char1_Row = find_row_index(playfairKey, char[0])
                char1_Column = find_column_index(playfairKey, char[0])
                char2_Row = find_row_index(playfairKey, char[1])
                char2_Column = find_column_index(playfairKey, char[1])

                if char1_Row == char2_Row:
                    char[0] = playfairKey[char1_Row][(char1_Column - 1)%5]
                    char[1] = playfairKey[char2_Row][(char2_Column - 1)%5]
                elif char1_Column == char2_Column:
                    char[0] = playfairKey[(char1_Row - 1)%5][char1_Column]
                    char[1] = playfairKey[(char2_Row - 1)%5][char2_Column]
                else:
                    char[0] = playfairKey[char1_Row][char2_Column]
                    char[1] = playfairKey[char2_Row][char1_Column]

                decryptedText = decryptedText[:indexC[0]] + char[0] + decryptedText[indexC[0]+1:indexC[1]] + char[1] + decryptedText[indexC[1]+1:]
                c = 0
        else:
            i+=1

    return decryptedText

def str_to_matrix(string):
    matrix=[[0 for row in range(0,5)] for col in range(0,5)]
    i = 0
    j = 0
    count = 0

    while i<5:

        while j < 5:

            matrix[i][j] = string[count]
            count = count+1
            j=j+1
        i = i+1
        j = 0
    return matrix

secretKey = str_to_matrix("lgdbaqmhecurnifxvsokzywtp")# if you want own secret key, this function convert from string to matrix.
