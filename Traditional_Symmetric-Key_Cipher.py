#!/usr/bin/python3
__author__ = 'Ahmfrkyvz'
'''
  Copyright (c) 2015, Ahmet Faruk YAVUZ - http://aksapp.me/ * All rights reserved.

  Redistribution and use in source and binary forms, with or without
  modification, are permitted provided that the following conditions
  are met:
  1. Redistributions of source code must retain the above copyright
     notice, this list of conditions and the following disclaimer.
  2. Redistributions in binary form must reproduce the above copyright
     notice, this list of conditions and the following disclaimer in the
     documentation and/or other materials provided with the distribution.
  3. Neither the name of the copyright holder nor the names of its
     contributors may be used to endorse or promote products derived
     from this software without specific prior written permission.

  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
  ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
  FOR A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE
  COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
  (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
  SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
  HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
  STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
  OF THE POSSIBILITY OF SUCH DAMAGE.
'''

from tkinter import *
from tkinter.filedialog import *
from cipher_Caesar import *
from cipher_Multiplecative import *
from cipher_Affine import *
from cipher_AutoKey import *
from cipher_Playfair import *
from cipher_Vigenere import *
from cipher_Hill import *
from cipher_Rail_Fence import *

def aboutUs():
    top = Toplevel()
    top.title("About")
    top.geometry("200x70+150+150")
    top.resizable(False, False)
    label= Label(top, font= "Arial 10 bold")
    label.config(text = "Ahmet Faruk YAVUZ\nFethi Erdinç UZUN\n\n2015")
    label.pack()

    top.mainloop()

def openFile():
    '''DOSYA OKUMA İŞLEMLERİ UTF-8 FORMATINDADIR TEXTLERİN DE UTF-8 KODLANMASI GEREKİR.'''
    file = askopenfile(parent=root,mode='rb',filetypes = [('text files', '.txt')], title='Choose a file')
    if file != None:
        print(file.name)
        inputText = file.read().decode('utf-8')
        file.close()
        if inputText[0] == '﻿':
            inputText = inputText[1:]
        outputTextView.delete(0.0, END)
        inputTextView.delete(0.0, END)
        inputTextView.insert(INSERT, inputText)

def saveFile():
    '''DOSYAYI UTF-8 KODLAYARAK KAYDEDİYOR.'''
    file = asksaveasfile(parent=root, mode='wb', filetypes = [('text files', '.txt')], title="Save the text as...")
    if file != None:
        print(file.name)
        outputText = outputTextView.get(0.0, END)
        file.write(outputText.encode('utf-8'))
        file.close()

def selectedType():

    labelSelectedText = spinnerSelectType.get()
    labelSelectedType.config(anchor= 'nw', text = "Chosen Type: " + labelSelectedText)
    if labelSelectedText == cipherList[0] or labelSelectedText == cipherList[1] or labelSelectedText == cipherList[3] or labelSelectedText == cipherList[5]:
        stateKey1 = NORMAL
        stateKey2 = DISABLED
    elif labelSelectedText == cipherList[4] or labelSelectedText == cipherList[6] or labelSelectedText == cipherList[7]:
        stateKey1 = DISABLED
        stateKey2 = DISABLED
    else:
        stateKey1 = NORMAL
        stateKey2 = NORMAL
    entryKey1.config(state=stateKey1)
    entryKey2.config(state=stateKey2)

def selectCoding():
    if var.get() == 1:
        labelInText = "Plaintext :"
        labelIn.config(text = labelInText)
        labelOutText = "Encrypted Text :"
        labelOut.config(text = labelOutText)
        btnText = "Encode"
        btnCrypto.config(text = btnText, command = encodeText)
    else:
        labelInText = "Encrypted Text :"
        labelIn.config(text = labelInText)
        labelOutText = "Decrypted Text :"
        labelOut.config(text = labelOutText)
        btnText = "Decode"
        btnCrypto.config(text = btnText, command = decodeText)

def keyControl(key, type):
    labelOutputMessage.config(text = "MESSAGE: " + "Please select encryption/decryption method")
    if type == "t":
        if key == "":
            print("Please input key value...")
            labelOutputMessage.config(text = "ERROR: " + "Please input key value...")
            return "error"
        else:
            return key
    else:
        if key.isdigit():
            if int(key) >= 0 and int(key) < 26:
                return int(key)
            else:
                print("Key value have to between 0-25...")
                labelOutputMessage.config(text = "ERROR: " + "Key value have to between 0-25...")
                return -1
        else:
            print("Key value have to an integer...")
            labelOutputMessage.config(text = "ERROR: " + "Key value have to an integer...")
            return -1

def encodeText():
    labelSelectedText = spinnerSelectType.get()
    plainText = inputTextView.get(0.0, END)
    outputTextView.delete(0.0, END)

    if labelSelectedText == cipherList[0]:
        key1 = keyControl(entryKey1.get(), 'n')
        if key1 > -1:
            encryptedText = caesar_cipher(plainText, key1)
            outputTextView.insert(INSERT, encryptedText)

    elif labelSelectedText == cipherList[1]:
        key1 = keyControl(entryKey1.get(), 'n')
        if key1 > -1:
            encryptedText = multiplicative_cipher(plainText, key1)
            outputTextView.insert(INSERT, encryptedText)

    elif labelSelectedText == cipherList[2]:
        key1 = keyControl(entryKey1.get(), 'n')
        key2 = keyControl(entryKey2.get(), 'n')
        if key1 > -1 and key2 > -1:
            encryptedText = affine_cipher(plainText, key1, key2)
            outputTextView.insert(INSERT, encryptedText)

    elif labelSelectedText == cipherList[3]:
        key1 = keyControl(entryKey1.get(), 'n')
        if key1 > -1:
            encryptedText = autokey_cipher(plainText, key1)
            outputTextView.insert(INSERT, encryptedText)

    elif labelSelectedText == cipherList[4]:
        encryptedText = playfair_cipher(plainText, 'x')
        outputTextView.insert(INSERT, encryptedText)

    elif labelSelectedText == cipherList[5]:
        key1 = keyControl(entryKey1.get(), 't')
        if key1 != "error":
            encryptedText = vigerene_cipher(plainText, key1)
            outputTextView.insert(INSERT, encryptedText)

    elif labelSelectedText == cipherList[6]:
        encryptedText = hill_cipher(plainText)
        outputTextView.insert(INSERT, encryptedText)

    elif labelSelectedText == cipherList[7]:
        encryptedText = rail_fence_cipher(plainText)
        outputTextView.insert(INSERT, encryptedText)

    else:
        return

def decodeText():
    labelSelectedText = spinnerSelectType.get()
    encryptedText = inputTextView.get(0.0, END)
    outputTextView.delete(0.0, END)

    if labelSelectedText == cipherList[0]:
        key1 = keyControl(entryKey1.get(), 'n')
        if key1 > -1:
            plainText = decrypt_caesar_cipher(encryptedText, key1)
            outputTextView.insert(INSERT, plainText)

    elif labelSelectedText == cipherList[1]:
        key1 = keyControl(entryKey1.get(), 'n')
        if key1 > -1:
            plainText = decrypt_multiplicative_cipher(encryptedText, key1)
            outputTextView.insert(INSERT, plainText)

    elif labelSelectedText == cipherList[2]:
        key1 = keyControl(entryKey1.get(), 'n')
        key2 = keyControl(entryKey2.get(), 'n')
        if key1 > -1 and key2 > -1:
            plainText = decrypt_affine_cipher(encryptedText, key1, key2)
            outputTextView.insert(INSERT, plainText)

    elif labelSelectedText == cipherList[3]:
        key1 = keyControl(entryKey1.get(), 'n')
        if key1 > -1:
            plainText = decrypt_autokey_cipher(encryptedText, key1)
            outputTextView.insert(INSERT, plainText)

    elif labelSelectedText == cipherList[4]:
        plainText = decrypt_playfair_cipher(encryptedText)
        outputTextView.insert(INSERT, plainText)

    elif labelSelectedText == cipherList[5]:
        key1 = keyControl(entryKey1.get(), 't')
        if key1 != "error":
            plainText = decrypt_vigerene_cipher(encryptedText, key1)
            outputTextView.insert(INSERT, plainText)

    elif labelSelectedText == cipherList[6]:
        plainText = decrypt_hill_cipher(encryptedText)
        outputTextView.insert(INSERT, plainText)

    elif labelSelectedText == cipherList[7]:
        plainText = decrypt_rail_fence_cipher(encryptedText)
        outputTextView.insert(INSERT, plainText)

    else:
        return
'''__________________________________________________________________________________________'''

cipherList = [("Caesar Cipher"), ("Multiplicative Cipher"), ("Affine Cipher") , ("Autokey Cipher"),
              ("Playfair Cipher") , ("Vigenere Cipher") , ("Hill Cipher") , ("Rail Fence Cipher") ]

'''STATES OF KEYS'''
stateKey1 = NORMAL
stateKey2 = DISABLED

'''MAIN WINDOW'''
root = Tk()
root.config(background = "#00728F")
root.resizable(False, False)
root.title("Traditional Symmetric-Key Ciphers")
root.geometry("900x600+150+50")

'''MENU TOOLBAR'''
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save as", command=saveFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=aboutUs)
menubar.add_cascade(label="Help", menu=helpmenu)
root.config(menu=menubar)

'''CIPHER TYPE'''
labelCipherType = Label(root, font= "Helvetica 12 bold", bg = "#85ADAD")
labelCipherType.config(text = "Select Cipher Type : ")
labelCipherType.place(relx=0.02, rely=0.04, relwidth=0.18)

frameSelectType = Frame(root, bg = "#85ADAD")
frameSelectType.place(relx=0.22, rely=0.04,)
spinnerSelectType = Spinbox(frameSelectType, font= "Helvetica 12 bold", values = cipherList[0:], wrap = TRUE, state = "readonly", command = selectedType)
spinnerSelectType.pack()
labelSelectedText = spinnerSelectType.get()

'''MESSAGES LABEL'''
labelSelectedType = Label(root, font= "Helvetica 10 bold", bg = "#85ADAD")
labelSelectedType.config(anchor= 'nw', text = "Chosen Type: " + labelSelectedText)
labelSelectedType.place(relx=0.02, rely=0.90, relwidth=0.96, relheight=0.04)
labelOutputMessage = Label(root, font= "Helvetica 10 bold", bg = "#799696")
labelOutputMessage.config(anchor= 'nw', text = "MESSAGE: " + "Please select encryption/decryption method")
labelOutputMessage.place(relx=0.02, rely=0.94, relwidth=0.96, relheight=0.04)

'''1st KEY'''
frameKey1 = Frame(root, bg = "#85ADAD")
frameKey1.place(relx=0.02, rely=0.12, relwidth = 0.22)
labelSelectKey1 =Label(frameKey1, bg = "#85ADAD")
labelSelectKey1.config(text = "Input 1st Key: ", font= "Helvetica 12 bold")
labelSelectKey1.pack(side = LEFT)
entryKey1 = Entry(frameKey1)
entryKey1.config(state=stateKey1)
entryKey1.pack(side = RIGHT)

'''2nd KEY'''
frameKey2 = Frame(root, bg = "#85ADAD")
frameKey2.place(relx=0.26, rely=0.12, relwidth = 0.22)
labelSelectKey2 =Label(frameKey2, bg = "#85ADAD", font= "Helvetica 12 bold")
labelSelectKey2.config(text = "Input 2nd Key: ")
labelSelectKey2.pack(side = LEFT)
entryKey2 = Entry(frameKey2)
entryKey2.config(state=stateKey2)
entryKey2.pack(side = RIGHT)

'''ENCODE-DECODE RADIOBUTTON'''
var = IntVar()
frameSelectCoding = Frame(root,bg = "#00728F")
frameSelectCoding.place(relx=0.02, rely=0.20, relheight = 0.10)
rbEnconding = Radiobutton(frameSelectCoding, bg = "#00728F", font= "Helvetica 12 bold", text="Encryption",
                                                variable=var, value=1, indicatoron=1, command = selectCoding)
rbEnconding.pack(anchor = 'w')
rbEnconding.select()
rbDeconding = Radiobutton(frameSelectCoding, bg = "#00728F", font= "Helvetica 12 bold", text="Decryption",
                                                variable=var, value=2, indicatoron=1, command = selectCoding)
rbDeconding.pack(anchor = 'w')

'''LEFT TEXTBOX (INPUT)'''
labelInText = "Plaintext :"
labelIn = Label(root, bg ="#85ADAD", font= "Helvetica 12 bold")
labelIn.config(text = labelInText)
labelIn.place(relx=0.02, rely=0.36)
inputTextView = Text(root, bg="#E6E6E6")
inputTextView.place(relx=0.02, rely=0.40, relheight=0.40, relwidth=0.46)

'''RIGHT TEXTBOX (OUTPUT)'''
labelOutText = "Encrypted Text :"
labelOut = Label(root, bg ="#85ADAD", font= "Helvetica 12 bold")
labelOut.config(text = labelOutText)
labelOut.place(relx=0.52, rely=0.36)
outputTextView = Text(root, bg="#E6E6E6")
outputTextView.place(relx=0.52, rely=0.40, relheight=0.40, relwidth=0.46)

'''ENCODE-DECODE BUTTON'''
btnText = "Encode"
btnCrypto = Button(root, bg ="#003948",fg = "white", font= "Helvetica 12 bold")
btnCrypto.config(text = btnText, command = encodeText)
btnCrypto.place(bordermode=OUTSIDE, relx=0.40, rely=0.82, relwidth=0.08)


mainloop()
